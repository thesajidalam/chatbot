# 🌌 Gemini Chatbot  

[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)](https://www.python.org/)  
[![Flask](https://img.shields.io/badge/Flask-2.3.3-black?logo=flask)](https://flask.palletsprojects.com/)  
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  
[![Google Gemini](https://img.shields.io/badge/Powered%20by-Google%20Gemini-orange?logo=google)](https://ai.google.dev/)  

A sleek, modern chatbot powered by **Google’s Gemini API** and wrapped with a **Flask** web interface.  
Built for developers, students, and AI enthusiasts who want a lightweight but powerful conversational AI app.  

---

## 🚀 Features  

- ⚡ **Google Gemini API Integration** — seamless conversation handling.  
- 🖥️ **Flask Web App** — clean and minimal backend.  
- 🎨 **Beautiful UI** — responsive HTML/CSS front-end.  
- 🔒 **Environment Variable Support** — keep your API keys secure.  
- 🛠️ **Modular Design** — separated logic (`gemini_handler.py`) and routes (`app.py`).  

---

## 📂 Project Structure  

gemini-chatbot/
│
├── app.py # Flask entry point
├── gemini_handler.py # Gemini API wrapper & logic
├── requirements.txt # Python dependencies
├── templates/
│ └── index.html # Frontend UI
├── static/
│ └── style.css # Styling for the chatbot
└── .env (optional) # Store your API key securely

yaml
Copy
Edit

---

## 🛠️ Setup Instructions  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/your-username/gemini-chatbot.git
cd gemini-chatbot
2️⃣ Create & Activate Virtual Environment (Recommended)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Configure Environment Variables
Create a .env file in the root directory and add your Google Gemini API key:

env
Copy
Edit
GOOGLE_API_KEY=your_api_key_here
🔑 Don’t have a key? Get one here.

5️⃣ Run the Application
bash
Copy
Edit
python app.py
6️⃣ Open in Browser
Navigate to:

👉 http://localhost:5000

🖥️ Usage
Enter your message in the chatbot UI.

Hit Send to interact with Gemini.

Get real-time AI-powered responses.

Modify style.css for full UI customization.

🎨 Screenshots
(Add screenshots/gifs of the chatbot interface here)

📌 Requirements
Python 3.8+

Flask 2.3.3

Requests 2.31.0

google-generativeai 0.3.2

python-dotenv 1.0.0

🤝 Contributing
Contributions are welcome! Feel free to:

Open issues

Submit pull requests

Suggest UI/UX improvements

📜 License
This project is licensed under the MIT License.

✨ Credits
Built with ❤️ using Flask + Google Gemini API

Designed for developers who love AI + Clean UI
