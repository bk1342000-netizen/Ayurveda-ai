# वैद्य सहायक | Ayurvedic AI Coach

AI-powered Ayurvedic health assistant with 2,000+ authentic Sanskrit shlokas from Charaka Samhita, Sushruta Samhita, and Ashtanga Hridaya.

🌿 **Live Demo:** Coming soon
📱 **WhatsApp:** Send "ज्वर" to +91-XXXXX

## Features

- 🔍 **Sanskrit Shloka Search** - RAG-based retrieval
- 🗣️ **Hindi Voice Support** - Speak your symptoms
- 📖 **Pathya-Apathya** - Diet guidance for each condition
- ✅ **Vaidya Verified** - Every shloka reviewed by BAMS doctors
- 📱 **WhatsApp Bot** - Works on 2G, no app needed
- 🎵 **Sanskrit Pronunciation** - Audio for each shloka

## Quick Start

### Option 1: Use in Browser (No install)
1. Download `index.html` and `knowledge.json`
2. Open `index.html` in Chrome
3. Search for "ज्वर", "कास", "अजीर्ण"

### Option 2: Deploy to Railway
```bash
git clone https://github.com/bk1342000-netizen/Ayurveda-ai.git
cd Ayurveda-ai
docker-compose up

├── backend/          # FastAPI + Qdrant
├── frontend/         # Next.js UI
├── whatsapp/         # Twilio bot
├── scraper/          # Charaka Samhita scraper
└── knowledge.json    # 238 shlokas (expanding to 2000)


---

### After pasting:

1. **Scroll down**
2. Tap **"Commit changes..."** (green button)
3. Tap **"Commit changes"** again

### Next step - Add your first file:

After README is saved:
1. Tap the **"+"** icon (top right in your screenshot)
2. Tap **"Add file"** → **"Create new file"**
3. Name it: `index.html`
4. Paste the HTML code I gave you earlier
5. Commit

**Want me to give you the `index.html` code to paste next?** Just say "yes" and I'll provide it ready to copy.
