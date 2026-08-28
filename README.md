# Gemini AI Chatbot

A single-file AI chatbot that talks to **Google Gemini** straight from your browser. Paste your Gemini API key, press Enter, and get real AI answers — no backend, no build step, no dependencies.

Built by [@thesajidalam](https://github.com/thesajidalam) · [github.com/thesajidalam](https://github.com/thesajidalam)

## Features

- Real requests to `https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent`
- Chat history kept for multi-turn conversations
- Typing indicator, loading state and clear error messages
- **Enter** to send
- **New chat** button to clear the conversation
- Your API key is saved in browser `localStorage` (never committed, never sent anywhere except Google)
- **Remove key** / **Replace key** options to wipe local data
- Dark, responsive, Telegram-style chat UI
- Pure vanilla HTML + CSS + JavaScript, single file, zero dependencies (Font Awesome CDN only)

## Quick start

1. Open `index.html` in any modern browser (Chrome, Firefox, Edge, Safari).
2. Paste your Gemini API key into the key bar and click **Save & start**.
3. Type a message and press **Enter**.

## Getting a Gemini API key from Google AI Studio

1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey) and sign in with your Google account.
2. Click **Create API key** (choose your Google Cloud project, or create one on the spot).
3. Copy the generated key — it starts with `AIza...`.
4. Paste it into the app. That's it.

> The key is stored only in your browser's `localStorage`. It is **never written to any file in this repo** — use **Remove key** whenever you're done to wipe it locally.

## Security

- Messages go **directly** from your browser to Google's servers — no proxy, no intermediary.
- Your API key lives only in `localStorage` on your own machine.
- Nothing is committed, logged or uploaded anywhere except Google.
- GitHub's secret scanning / review safety: this repo contains **no** real keys (`index.html` reads yours at runtime).

## Deployment

Since it's a single static file you can run it anywhere:

- Double-click `index.html` to open it locally
- Drop it on GitHub Pages / Netlify / Vercel static hosting
- Serve it from any basic web server

## Project structure

```
chatbot/
├── index.html   # The entire app (UI + logic, single file)
├── README.md
└── .gitignore
```

## Cost & limits

Gemini API free tier applies per Google's current pricing. `gemini-1.5-flash` is the fast, low-cost model used here by default.

## License

MIT — free to use, modify and share.

## Credits

Built with ❤️ by **[@thesajidalam](https://github.com/thesajidalam)** on top of the **Google Gemini API**.