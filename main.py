import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Load JSON data
with open('./data/dummy.json') as f:
    data = json.load(f)

# Set up the ChromeDriver service
chrome_service = Service('C:/Program Files/ChromeDriver/chromedriver.exe')

# Initialize the WebDriver
driver = webdriver.Chrome(service=chrome_service)

# Open the web page with the form
driver.get('https://www.digitalunite.com/practice-webform-learners')

# Fill the form fields
driver.find_element(By.ID, 'edit-name').send_keys(data['name'])

# Keep the browser window open indefinitely
try:
    while True:
        pass
except KeyboardInterrupt:
    pass

# Close the browser (optional, as the script can be stopped manually)
driver.quit()
