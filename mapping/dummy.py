from selenium.webdriver.common.by import By

def fill_form(driver, data, element_xpath=None, data_fields=None, strategy=None):
    if strategy:
        # Use the provided strategy to transform data and fill the form
        strategy(driver, data)
    elif element_xpath and data_fields:
        if isinstance(data_fields, list):
            # Handle multiple fields
            for field in data_fields:
                element = driver.find_element(By.XPATH, element_xpath)
                element.send_keys(data.get(field, ''))
        else:
            # Handle single field
            element = driver.find_element(By.XPATH, element_xpath)
            element.send_keys(data.get(data_fields, ''))
    else:
        raise ValueError("Either element_xpath and data_fields or strategy must be provided.")
