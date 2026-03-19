from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

leads_db = [
    {
        "title": "Website Development",
        "description": "Need a business website",
    },
    {
        "title": "Mobile App",
        "description": "Need Android app for ecommerce",
    }
]

def score_lead(lead):
    score = len(lead["description"]) % 100
    return {"score": score, "reason": "Based on description length"}

def generate_pitch(lead):
    return f"Hi, I can help you with {lead['title']} project."

@app.get("/leads")
def get_leads():
    result = []

    for lead in leads_db:
        score_data = score_lead(lead)
        pitch = generate_pitch(lead)

        result.append({
            "title": lead["title"],
            "score": score_data["score"],
            "reason": score_data["reason"],
            "pitch": pitch
        })

    return result