from fastapi import FastAPI,HTTPException 
from pydantic import BaseModel
from dotenv import load_dotenv
import google.generativeai as genai
import os
import json

# Load your API key from .env file
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create the FastAPI app
app = FastAPI()

#initialize gemini model
model = genai.GenerativeModel("gemini-2.5-flash")

# This defines what the request body should look like
class TextInput(BaseModel):
    text: str

# Root endpoint — just to confirm API is running
@app.get("/")
def home():
    return {"message": "AI Summarizer API is running"}

# Summarize endpoint — this is the main feature
@app.post("/summarize")
def summarize(input: TextInput):
    
    prompt = f"Summarize the following text in 3-4 sentences:\n\n{input.text}"
    response = model.generate_content(prompt)
    return {"summary": response.text}


@app.post("/summarize/bullets")
def bullets(input: TextInput):
    prompt = f"Summarize the following text in 3-4 bullets:\n\n{input.text}"
    response = model.generate_content(prompt)
    lines = response.text.split("\n")
    bullets = []
    for line in lines :
        if line.startswith("*") : 
            bullets.append(line)
    return {"bullets": bullets}

@app.post("/summarize/sentiment")
def sentiment(input: TextInput):
    prompt = f"Analyse the Sentiment of the input text and return response only in json with two fields exactly sentiment and reason:\n\n{input.text}"
    response = model.generate_content(prompt)
    cleaned = response.text.replace("```json", "")
    cleaned = cleaned.replace("```","")
    try : 
        result = json.loads(cleaned)
    except : 
        raise HTTPException(status_code=500, detail="Improper Gemini Response")    
    return result