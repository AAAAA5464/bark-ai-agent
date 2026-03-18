from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()
options.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

service = Service("./chromedriver.exe")

driver = webdriver.Chrome(service=service, options=options)

driver.get("https://google.com")