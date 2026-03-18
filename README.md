# Bark AI Lead Evaluation Agent

This project demonstrates a Proof-of-Concept AI agent that automates the discovery and evaluation of service leads.

Features:
- Browser automation using Selenium
- Lead evaluation scoring (0–1)
- Personalized pitch generation

How to run:

pip install -r requirements.txt

python main.py

## Setup

1. Create a `config.py` file with your credentials:

```python
OPENAI_API_KEY = "YOUR_API_KEY"
BARK_EMAIL = "your_email"
BARK_PASSWORD = "your_password"