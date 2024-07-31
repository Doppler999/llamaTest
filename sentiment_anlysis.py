import subprocess
import re

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

# Example usage
if __name__ == "__main__":
    text = "I love this product! It's really amazing and works perfectly."
    sentiment = analyze_sentiment(text)
    print(f"The sentiment is: {sentiment}")
