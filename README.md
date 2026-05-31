# AI Summarizer API

A REST API that uses Google Gemini to summarize text.

## Tech Stack
- Python
- FastAPI
- Google Gemini 2.5 Flash
- Uvicorn

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

## Setup

1. Clone the repo
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `venv\Scripts\activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Create a `.env` file with your `GEMINI_API_KEY`
6. Run: `uvicorn main:app --reload`