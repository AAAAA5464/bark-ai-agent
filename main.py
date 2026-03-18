from scraper import BarkScraper
from ai_agent import score_lead, generate_pitch

BARK_EMAIL = ""
BARK_PASSWORD = ""

scraper = BarkScraper(BARK_EMAIL, BARK_PASSWORD)

scraper.open_dashboard()

try:
    leads = scraper.scrape_leads()

    for lead in leads:

        print("\nLead:", lead["title"])

        result = score_lead(lead)

        print("Score:", result["score"])
        print("Reason:", result["reason"])

        pitch = generate_pitch(lead)

        print("\nGenerated Pitch:")
        print(pitch)

except Exception as e:
    print("ERROR OCCURRED:", e)

input("Press ENTER to close...")