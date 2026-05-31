from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import google.generativeai as genai
import os

# Load your API key from .env file
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create the FastAPI app
app = FastAPI()

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
    model = genai.GenerativeModel("gemini-2.5-flash")
    prompt = f"Summarize the following text in 3-4 sentences:\n\n{input.text}"
    response = model.generate_content(prompt)
    return {"summary": response.text}