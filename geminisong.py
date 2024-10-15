from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import re
from dotenv import load_dotenv
import os


load_dotenv(dotenv_path="../.env")
app = Flask(__name__)
CORS(app)  # This enables CORS for all routes
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Replace with your actual API key


# Model configuration for lyrics generation
generation_config = {
  "temperature": 0.7,
  "top_p": 0.9,
  "top_k": 40,
  "max_output_tokens": 2048,
  "response_mime_type": "text/plain",
}

def generate_lyrics(description, language, genre, keywords, mood, negative_prompt):
  try:
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel(
      model_name="gemini-1.5-flash",
      generation_config=generation_config
    )
    chat_session = model.start_chat(history=[])
    prompt = f"""Write a song in the {genre} genre about {description} in {language}. 
    The mood of the song should be {mood}. 
    Include these keywords or themes: {keywords}. 
    Avoid using these words or phrases: {negative_prompt}.

    Generate 3 different versions of the lyrics.
    Format your response exactly as follows, with three dashes (---) separating each version:

    [Lyrics for version 1]

    ---

    [Lyrics for version 2]

    ---

    [Lyrics for version 3]
    """
    response = chat_session.send_message(prompt)
    
    # Split the response into versions using the separator
    versions = response.text.split('---')
    
    # Clean up each version
    versions = [v.strip() for v in versions if v.strip()]
    
    # Ensure we have exactly 3 versions
    if len(versions) > 3:
      versions = versions[:3]  # Keep only the first 3 versions
    elif len(versions) < 3:
      versions += [""] * (3 - len(versions))  # Pad with empty strings if less than 3
    
    return versions
  except Exception as e:
    return [f"Error generating lyrics: {e}"] * 3

def refine_lyrics(current_lyrics, keywords, mood, negative_prompt):
  try:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel(
      model_name="gemini-1.5-flash",
      generation_config=generation_config
    )
    chat_session = model.start_chat(history=[])
    prompt = f"""Refine the following lyrics:

    {current_lyrics}

    Incorporate these keywords or themes: {keywords}
    Maintain or adjust to this mood: {mood}
    Avoid using these words or phrases: {negative_prompt}"""
    response = chat_session.send_message(prompt)
    return response.text
  except Exception as e:
    return f"Error refining lyrics: {e}"

@app.route('/api/generate_lyrics', methods=['POST'])
def generate_lyrics_api():
    description = request.form.get('description')
    language = request.form.get('language')
    genre = request.form.get('genre')
    keywords = request.form.get('keywords')
    mood = request.form.get('mood')
    negative_prompt = request.form.get('negative_prompt')
    if not all([description, language, genre, keywords, mood]):
        return jsonify({"error": "Missing required fields"}), 400

    lyrics_versions = generate_lyrics(description, language, genre, keywords, mood, negative_prompt)
    
    if all(v.startswith("Error generating lyrics:") for v in lyrics_versions):
        return jsonify({"error": lyrics_versions[0]}), 500
    
    return jsonify({"lyrics": lyrics_versions})

@app.route('/api/refine_lyrics', methods=['POST'])
def refine_lyrics_api():
  current_lyrics = request.form.get('current_lyrics')
  keywords = request.form.get('keywords')
  mood = request.form.get('mood')
  negative_prompt = request.form.get('negative_prompt')
  if not all([current_lyrics, keywords, mood]):
    return jsonify({"error": "Missing required fields"}), 400
  refined_lyrics = refine_lyrics(current_lyrics, keywords, mood, negative_prompt)
  return jsonify({"refined_lyrics": refined_lyrics})
 
app = app