# FlexFill

## Description

FlexFill is a flexible form-filling script that uses Selenium WebDriver to automate the process of filling out web forms. The script supports configurable mappings for form fields and allows for pre-actions, such as clicking buttons to open forms, before starting the form-filling process.

## Requirements

- Python 3.x
- Selenium
- PyYAML
- Chrome WebDriver

## Usage

1. **Install the required Python packages:**
    ```sh
    pip install selenium pyyaml
    ```

2. **Configure the `configs.yaml` file:**
    - `data_file`: Path to the JSON file containing form data.
    - `chrome_driver_path`: Path to the Chrome WebDriver executable.
    - `form_url`: URL of the web page with the form.
    - `mapping`: Path to the Python file containing field mappings.
    - `pre_action`: (Optional) Path to the Python file containing pre-action logic.

3. **Run the script:**
    ```sh
    python main.py
    ```

### Example `configs.yaml`

```yaml
data_file: './data/dummy.json'
chrome_driver_path: 'C:/Program Files/ChromeDriver/chromedriver.exe'
form_url: 'https://www.digitalunite.com/practice-webform-learners'
mapping: './mapping/dummy.py'
pre_action: './pre_action.py'
```

## Notes

- Ensure that the paths in the configs.yaml file are correctly set according to your environment.
- The pre-action script is optional. If no pre-action is needed, you can omit the pre_action key or provide an empty script.
