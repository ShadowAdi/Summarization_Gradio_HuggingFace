from dotenv import load_dotenv
import os
import gradio as gr
import requests
from newspaper import Article
import time
from langdetect import detect


# Load environment variables from .env file
load_dotenv()
API_KEY = os.getenv('API_KEY')

# Define the Hugging Face API URL
API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
API_URL_TRANSLATION = "https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-zh-en"


# Set up headers for the API request
headers = {"Authorization": f"Bearer {API_KEY}"}

# Function to query the Hugging Face API
def query(payload):
    for _ in range(5):  # Try 5 times
        response = requests.post(API_URL, headers=headers, json=payload)
        result = response.json()
        if 'error' in result and 'currently loading' in result['error']:
            time.sleep(5)  # Wait for 5 seconds before retrying
        else:
            return result
    return {"error": "Model is still loading. Please try again later."}



# Function to summarize text
def summarize(text, minL=20, maxL=300):
    output = query({
        "inputs": text,
        "parameters": {
            "min_length": minL,
            "max_length": maxL
        }
    })
    if "error" in output:
        return f"Error: {output['error']}"
    if not isinstance(output, list) or not output:
        return "Error: Unexpected response format."
    if "summary_text" not in output[0]:
        return "Error: 'summary_text' key not found in the response."
    return output[0]['summary_text']

def Choices(choice,input_text,minL,maxL):
    if choice=="URL":
        try:
            article=Article(input_text,language="en")
            article.download()
            article.parse()
            article.nlp()
            text=article.text
        except Exception as e:
            return f"Error: Unable to fetch article. {str(e)}"
    else:
        text=input_text
    return summarize(text, minL, maxL)

# Create Gradio interface
demo = gr.Interface(
    fn=Choices,
    inputs=[
        gr.Radio(choices=["URL", "Paragraph"], label="Input Type", value="URL"),
        gr.Textbox(lines=10, placeholder="Enter text here..."),
        gr.Number(value=20, label="Minimum Length"),
        gr.Number(value=300, label="Maximum Length"),
    ],
    outputs="textbox",
    title="Text Summarizer",
    description="Enter text to summarize using Hugging Face BART model."
)

# Launch the interface
demo.launch()
