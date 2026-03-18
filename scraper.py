from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time


class BarkScraper:

    def __init__(self, email, password):

        self.email = email
        self.password = password

        options = Options()
        options.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

        options.add_argument("--start-maximized")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-extensions")

        service = Service(r"C:\Users\Aman\Desktop\bark-ai-agent\drivers\chromedriver.exe")

        self.driver = webdriver.Chrome(service=service, options=options)

    def open_dashboard(self):

        print("Opening Bark homepage...")

        self.driver.get("https://www.bark.com")

        time.sleep(5)

    def scrape_leads(self):

        print("Collecting sample leads...")

        leads = []

        for i in range(3):

            lead = {
                "title": f"Website Development Project {i+1}",
                "description": "Client needs a professional website for business",
                "budget": "$2500",
                "location": "London"
            }

            leads.append(lead)

        return leads