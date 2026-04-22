# 🏥 MediScan AI Malaysia

> AI-powered medical image analysis for rural Malaysian healthcare workers — built with Google Gemini API

[![Live Demo](https://img.shields.io/badge/Live-Demo-green)](https://mediscan-ai-malaysia.run.app)
[![Track](https://img.shields.io/badge/Track-Healthcare-blue)]()
[![Built With](https://img.shields.io/badge/Built%20With-Gemini%20API-orange)]()

---

## 🩺 Problem

Over 3 million Malaysians in rural areas lack access to specialist doctors.
Frontline health workers at rural clinics often have no tools to assist with
medical image interpretation — leading to delayed diagnoses and poor outcomes.

---

## 💡 Solution

**MediScan AI Malaysia** is a web application that allows frontline health
workers to upload medical images (X-rays, skin conditions, wound photos) and
receive instant AI-assisted analysis powered by **Google Gemini API**.

No specialist required. No waiting. Just upload and get insights.

---

## ✨ Features

- 📸 Upload any medical image (X-ray, skin, wound)
- 🤖 Instant AI analysis powered by Gemini 1.5 Pro
- 🇲🇾 Supports Bahasa Malaysia & English
- 📋 Generates structured clinical notes
- ☁️ Deployed on Google Cloud Run

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| AI Model | Google Gemini 1.5 Pro (via AI Studio) |
| Frontend | Streamlit |
| Backend | Python |
| Deployment | Google Cloud Run |
| Version Control | GitHub |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.11+
- Google AI Studio API Key ([Get one free](https://aistudio.google.com))

### Installation

```bash
git clone https://github.com/hafizkwar/mediscan-ai-malaysia.git
cd mediscan-ai-malaysia/gemini/sample-apps/gemini-streamlit-cloudrun
pip install -r requirements.txt
```

### Run Locally

```bash
export GOOGLE_API_KEY=your_api_key_here
streamlit run app.py
```

---

## ☁️ Deployment

Deployed live on Google Cloud Run:
🔗 **https://mediscan-ai-malaysia.run.app**

---

## 🎯 Hackathon

**Project 2030: MyAI Future Hackathon**
- Organized by: Google Developer Groups on Campus UTM
- Track: **Healthcare**
- Team: Hafiz Kamar

---

## 🇲🇾 Impact

> "Malaysia Madani — Berkhidmat Untuk Negara"

This project directly supports **Malaysia's digital health transformation**
by bringing AI-assisted diagnostics to underserved rural communities,
aligned with the **MyDigital Blueprint** and **Sustainable Development Goal 3**
(Good Health and Well-Being).

---

## 📄 License

This project is based on [GoogleCloudPlatform/generative-ai](https://github.com/GoogleCloudPlatform/generative-ai)
and is licensed under the Apache 2.0 License.
Contributions welcome! See the [Contributing Guide](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/CONTRIBUTING.md).

## Getting help

Please use the [issues page](https://github.com/GoogleCloudPlatform/generative-ai/issues) to provide suggestions, feedback or submit a bug report.

## Disclaimer

This repository itself is not an officially supported Google product. The code in this repository is for demonstrative purposes only.
