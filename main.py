import json
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from mapping.dummy import fill_form

with open('configs.yaml', 'r') as f:
    config = yaml.safe_load(f)
with open(config['data_file']) as f:
    data = json.load(f)

chrome_service = Service(config['chrome_driver_path'])
driver = webdriver.Chrome(service=chrome_service)
driver.get(config['form_url'])

fill_form(driver, data)

try:
    while True:
        pass
except KeyboardInterrupt:
    pass

driver.quit()
