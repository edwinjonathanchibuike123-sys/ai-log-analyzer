import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

def read_logs(file_path):
    with open(file_path, "r") as f:
        return f.read()

def analyze_with_ai(log_content):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {
                "role": "user",
                "content": f"You are a DevOps engineer. Analyze these logs, identify errors, and give a short incident report:\n\n{log_content}"
            }
        ]
    }
    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers=headers,
        json=payload
    )
    result = response.json()
    print("RAW:", result)
    return result["choices"][0]["message"]["content"]

logs = read_logs("sample.log")
print("=== AI INCIDENT REPORT ===")
print(analyze_with_ai(logs))
