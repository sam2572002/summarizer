# AI Summarizer API

A REST API built with FastAPI and Google Gemini that generates AI-powered text summaries and sentiment analysis

## Tech Stack
- Python
- FastAPI
- Google Gemini 2.5 Flash
- Uvicorn
- Railway(deployment)

## How It Works
Send any text to the `/summarize` endpoint and get back a 3-4 sentence AI-generated summary.

## Endpoints

### GET /
Returns API status.

### POST /summarize
Accepts a JSON body and returns a summary.

**Request:**
```json
{
  "text": "Your text here"
}
```

**Response:**
```json
{
  "summary": "AI generated summary here"
}
```

### POST /summarize

Generates a concise 3–4 sentence summary of the provided text.

**Request**

```json
{
  "text": "Your text here"
}
```

**Response**

```json
{
  "summary": "AI-generated summary here"
}
```

---

### POST /summarize/bullets

Generates a bullet-point summary highlighting the key points from the provided text.

**Request**

```json
{
  "text": "Your text here"
}
```

**Response**

```json
{
  "summary": [
    "Key point 1",
    "Key point 2",
    "Key point 3"
  ]
}
```

---

### POST /summarize/sentiment

Analyzes the sentiment of the text and provides a concise summary.

**Request**

```json
{
  "text": "Your text here"
}
```

**Response**

```json
{
  "sentiment": "Positive",
  "summary": "AI-generated summary here"
}
```

## Setup

1. Clone the repo
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `venv\Scripts\activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Create a `.env` file with your `GEMINI_API_KEY`
6. Run: `uvicorn main:app --reload`

This API is deployed on Railway and can be accessed through the Railway-generated deployment URL.

## Example Use Cases

* Article summarization
* Blog and content summarization
* Meeting notes summarization
* Research paper summaries
* Sentiment analysis of customer feedback
* Social media sentiment analysis
* Bullet-point extraction of key information
