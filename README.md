# FlexFill

## Description
FlexFill is a Python script that uses Selenium to automate the process of filling out web forms. The script reads input data from a JSON file and fills specified form fields on a given web page. The browser window remains open indefinitely to allow for manual inspection and submission of the form.

## Requirements
- Python 3.x
- Selenium
- ChromeDriver

## Usage
1. **Install Selenium**:
    ```bash
    pip install selenium
    ```

2. **Download ChromeDriver**:
    - Download the appropriate version of ChromeDriver for your operating system from [ChromeDriver - WebDriver for Chrome](https://sites.google.com/chromium.org/driver/downloads).
    - Extract the downloaded file and place the ChromeDriver executable in a directory included in your system's PATH, or specify the path to the executable in the script.

3. **Prepare JSON Input File**:
    - Create a file named `dummy.json` in the `./data/` directory with the following content:
        ```json
        {
          "name": "John Doe",
          "email": "john.doe@example.com",
          "message": "Hello, this is a test message."
        }
        ```

4. **Modify and Run the Script**:
    - Ensure the script `main.py` is correctly set up:
        - path to the data file (e.g. `./data/dummy.json`)
        - path to the ChromeDriver executable (e.g. `C:/Program Files/ChromeDriver/chromedriver.exe`)
        - web page URL with the form to fill (e.g. `https://www.digitalunite.com/practice-webform-learners`)
        - data fields mapping to the form fields (e.g. `name`, `email`, `message`)

    - Run the script using Python:
        ```bash
        py ./src/main.py
        ```

    - The browser will open, fill in the `name` field, and remain open indefinitely. To stop the script and close the browser, press `Ctrl+C` in the terminal or command prompt.
