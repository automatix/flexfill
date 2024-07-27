from selenium.webdriver.common.by import By

def fill_form(driver, data):
    driver.find_element(By.ID, 'edit-name').send_keys(data['name'])
