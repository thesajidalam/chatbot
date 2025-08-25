from flask import Flask, render_template, request, jsonify
from gemini_handler import GeminiHandler
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Initialize Gemini handler
gemini_api_key = os.getenv("GEMINI_API_KEY", "AIzaSyBQuPu1lFRZveJ4GYrPSEfw5lgGne5hLBQ")
gemini = GeminiHandler(gemini_api_key)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    bot_response = gemini.get_response(user_message)
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
