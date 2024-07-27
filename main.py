import json
import yaml
import importlib.util
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from mapper import fill_form

with open('configs.yaml', 'r') as f:
    config = yaml.safe_load(f)
with open(config['data_file']) as f:
    data = json.load(f)

mapping_spec = importlib.util.spec_from_file_location("mapping", config['mapping'])
mapping = importlib.util.module_from_spec(mapping_spec)
mapping_spec.loader.exec_module(mapping)

chrome_service = Service(config['chrome_driver_path'])
driver = webdriver.Chrome(service=chrome_service)
driver.get(config['form_url'])

if 'pre_action' in config:
    pre_action_spec = importlib.util.spec_from_file_location("pre_action", config['pre_action'])
    pre_action = importlib.util.module_from_spec(pre_action_spec)
    pre_action_spec.loader.exec_module(pre_action)
    pre_action.execute_pre_action(driver)

for map_item in mapping.mappings:
    fill_form(driver, data, *map_item)

try:
    while True:
        pass
except KeyboardInterrupt:
    pass

driver.quit()
