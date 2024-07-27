import json
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Load configuration from configs.yaml
with open('configs.yaml', 'r') as f:
    config = yaml.safe_load(f)

# Load JSON data
with open(config['data_file']) as f:
    data = json.load(f)

# Set up the ChromeDriver service
chrome_service = Service(config['chrome_driver_path'])

# Initialize the WebDriver
driver = webdriver.Chrome(service=chrome_service)

# Open the web page with the form
driver.get(config['form_url'])

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
