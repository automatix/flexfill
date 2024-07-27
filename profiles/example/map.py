from selenium.webdriver.common.by import By

mappings = [
    ['//input[@id="edit-name"]', ['name']],  # Default case with no transformation
    ['//input[@id="edit-email"]', ['email'], lambda driver, data: driver.find_element(By.XPATH, '//input[@id="edit-email"]').send_keys(data.get('email', ''))],  # Custom strategy
]
