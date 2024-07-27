from selenium.webdriver.common.by import By

def fill_form(driver, data, element_xpath=None, data_fields=None, strategy=None):
    if strategy:
        strategy(driver, data)
    elif element_xpath and data_fields:
        if isinstance(data_fields, list):
            for field in data_fields:
                element = driver.find_element(By.XPATH, element_xpath)
                element.send_keys(data.get(field, ''))
        else:
            element = driver.find_element(By.XPATH, element_xpath)
            element.send_keys(data.get(data_fields, ''))
    else:
        raise ValueError("Either element_xpath and data_fields or strategy must be provided.")
