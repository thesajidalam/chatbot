# model_checker.py
import requests
import json

def list_available_models(api_key):
    """List all available models"""
    url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            models = response.json().get('models', [])
            print("Available models:")
            for model in models:
                print(f"Name: {model['name']}")
                print(f"Supported methods: {model.get('supportedGenerationMethods', [])}")
                print("---")
        else:
            print(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Exception: {str(e)}")

if __name__ == "__main__":
    api_key = "AIzaSyBQuPu1lFRZveJ4GYrPSEfw5lgGne5hLBQ"
    list_available_models(api_key)
