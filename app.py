from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import re
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('API_SECRET_KEY', 'default_secret_key')

# Enable CORS for all routes and origins
CORS(app)

def run_llama_model(prompt):
    # Command to run LLaMA via Ollama
    result = subprocess.run(['ollama', 'run', 'llama3.1:8b', prompt], capture_output=True, text=True)
    return result.stdout

def analyze_sentiment(text):
    # Craft a prompt for LLaMA to perform sentiment analysis
    prompt = f"Analyze the sentiment of the following text and return 'Positive', 'Negative', or 'Neutral':\n\n{text}\n\nSentiment:"

    # Generate a response using the LLaMA model
    response = run_llama_model(prompt)

    # Extract the sentiment label from the response
    sentiment = re.search(r"(Positive|Negative|Neutral)", response, re.IGNORECASE)
    return sentiment.group(0) if sentiment else "Unknown"

@app.route('/api/v1/sentiment', methods=['POST'])
def sentiment_api():
    data = request.json
    text = data.get('text', '')

    if not text:
        return jsonify({'error': 'No text provided'}), 400

    sentiment = analyze_sentiment(text)
    return jsonify({'sentiment': sentiment})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
