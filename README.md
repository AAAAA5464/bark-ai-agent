# 🚀 Bark AI Agent

## 📌 Overview
This project implements a **Bark AI Agent** that automates the process of:
- Lead ingestion (simulated via API/webhook)
- Lead scoring
- AI-based pitch generation
- Visualization through a React dashboard

It demonstrates a complete **end-to-end workflow** from lead input to actionable output.

---

## ⚙️ Tech Stack

- **Backend:** FastAPI (Python)
- **Frontend:** React.js
- **Integration:** Simulated Bark API/Webhook
- **Tools:** Axios, Uvicorn

---

## 🔄 Workflow

Bark Lead (Simulated)  
→ Backend Processing (FastAPI)  
→ Lead Scoring  
→ Pitch Generation  
→ API Response  
→ React Dashboard Display  

---

## ✨ Features

- 📥 Lead ingestion (API/webhook simulation)
- 📊 Automated lead scoring
- 💬 AI-generated personalized pitch
- 🖥️ Interactive React dashboard
- 🔗 End-to-end integration

---

## 🚀 How to Run

### 1️⃣ Clone the Repository

```bash

## Run Backend
cd backend
pip install -r ../requirements.txt
python -m uvicorn main:app --reload

👉 Open:
http://127.0.0.1:8000/docs

## Run Frontend
cd frontend
npm install
npm start

👉 Open:
http://localhost:3000
git clone hps://github.com/AAAAA5464/bark-ai-agent.git
cd bark-ai-agent
