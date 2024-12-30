# Lyrical Flask 🌐  

This is the Flask server for the **[Lyrical Application](https://github.com/Duality404/Lyrical)** , handling API requests to process user preferences and generate custom lyrics. The server interacts with the **Gemini API** for lyrics generation and is hosted on **Vercel** for seamless deployment and scalability.  

---

## Table of Contents  

1. [Features](#features)  
2. [Modules and Working](#modules-and-working)  
    * [User Input Processing](#user-input-processing)  
    * [Lyrics Generation](#lyrics-generation)
    * [Lyrics Refinement](#lyrics-refinement)  
3. [Installation](#installation)  
4. [Usage](#usage)  
5. [Deployment](#deployment)  

---

## Features  

- **API Integration**: Processes user input and communicates with the Gemini API.  
- **Real-Time Lyrics Generation**: Delivers responses quickly to ensure smooth user experiences.  
- **Scalable Deployment**: Hosted on Vercel for high availability and reliability.  
- **Lightweight Design**: Built using Flask for simplicity and efficiency.  

---

## Modules and Working  

### User Input Processing  

- Accepts user inputs like mood, style, and theme via POST requests.  
- Validates input to ensure proper formatting and completeness.  

### Lyrics Generation  

- Interacts with the **Gemini API** using the processed user input.  
- Returns generated lyrics in JSON format for further processing by the **Lyrical** Flutter application.

### Lyrics Refinement  

- Interacts with the **Gemini API** using the existing lyrics to refine them.  
- Returns refined lyrics in JSON format for further processing by the **Lyrical** Flutter application.  

---

## Installation  

1. **Clone the Repository**:  

    ```bash
    git clone https://github.com/Duality404/lyrical-flask.git
    cd lyrical-flask
    ```

2. **Set Up Virtual Environment (Optional)**:  

    ```bash
    python -m venv venv
    source venv/bin/activate    # On macOS/Linux
    venv\Scripts\activate       # On Windows
    ```

3. **Install Dependencies**:  

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure Environment Variables**:  

    Create a `.env` file in the root directory and add the following:  

    ```env
    GEMINI_API_KEY=your_gemini_api_key
    ```

    Replace `your_gemini_api_key` with your actual Gemini API key.  

---

## Usage  

1. **Run the Server Locally**:  

    ```bash
    python geminisong.py
    ```

2. **Interact with the API**:  

    Use tools like Postman or Curl to send POST requests to the endpoints:
     
    - **Generate Lyrics endpoint**:  
    ```bash
    curl -X POST http://localhost:5000/api/generate_lyrics \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "description=A heartfelt song about love" \
     -d "language=English" \
     -d "genre=Pop" \
     -d "keywords=love,romance,emotion" \
     -d "mood=romantic" \
     -d "negative_prompt=anger"
    ```

   **Sample Response**:  

    ```json
    {
    "lyrics": [
        "Version 1: Lyrics generated based on the provided inputs...",
        "Version 2: Another set of lyrics generated...",
        "Version 3: Final version of generated lyrics..."
    ]
    }
    ```
    - **Refine Lyrics endpoint**:  
    ```bash
    curl -X POST http://localhost:5000/api/refine_lyrics \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "current_lyrics=This is the original draft of the song lyrics" \
     -d "keywords=love,hope,joy" \
     -d "mood=happy" \
     -d "negative_prompt=sadness"
    ```

    **Sample Response**:  

    ```json
    {
    "refined_lyrics": "Refined version of the lyrics based on the updated inputs."
    }

    ```

---

## Deployment  

The server is deployed on **Vercel** for scalability and ease of access.  

### Steps to Deploy on Vercel:  

1. Install the Vercel CLI:  

    ```bash
    npm install -g vercel
    ```

2. Log in to Vercel:  

    ```bash
    vercel login
    ```

3. Deploy the Project:  

    ```bash
    vercel
    ```
