from openai import OpenAI
import json
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def score_lead(lead):

    return {
        "score": 0.85,
        "reason": "Budget above $2000 and relevant web development project"
    }


def generate_pitch(lead):

    pitch = f"""
Hi,

I saw your request about {lead['title']}.
I have experience building professional business websites and ecommerce platforms.

I would love to help you complete this project efficiently.

Best regards
"""

    return pitch