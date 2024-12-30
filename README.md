
<h1 align="center" style="font-weight: bold;">Lyrical ♪ </h1>

<p align="center">
<a href="#tech">Technologies</a>
<a href="#started">Getting Started</a>
<a href="#routes">API Endpoints</a>
<a href="#colab">Collaborators</a>
<a href="#contribute">Contribute</a> 
</p>


<p align="center">This repository contains the flask backend code for the web application lyrical</p>


<p align="center">
<a href="https://lyrical-omega.vercel.app/">📱 Visit this Project</a>
</p>

<h2 id="technologies">💻 Technologies</h2>

- Python
- Flask
- Gemini API

<h3>Cloning</h3>
```bash
git clone https://github.com/Duality404/lyrical-flask.git
```

<h3>Config .env variables</h2>

Create a .env file for storing the gemini api key

```yaml
GEMINI_API_KEY={your_api_key}
```

<h2 id="routes">📍 API Endpoints</h2>

Here you can list the main routes of your API, and what are their expected request bodies.
​
| route               | description                                          
|----------------------|-----------------------------------------------------
| <kbd>POST /api/generate_lyrics</kbd>     | sends post request to generate lyrics with appropriate fields
| <kbd>POST /api/refine_lyrics</kbd>     | sends post request to refine existing lyrics



<h3>Documentations that might help</h3>

[📝 Gemini API docs](https://ai.google.dev/gemini-api/docs)

[💾 Flask docs](https://flask.palletsprojects.com/en/stable/)
