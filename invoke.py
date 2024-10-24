from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
import json
import os

# Specify the port for remote debugging
desired_port = 9222 

# Create a new Chrome instance with remote debugging enabled
chrome_options = ChromeOptions()
chrome_options.add_argument(f'--remote-debugging-port={desired_port}')
chrome_options.add_experimental_option("detach", True)
driver_chrome = webdriver.Chrome(options=chrome_options)


driver_chrome.get("https://web.whatsapp.com")

# Save session info
driver_info = {
    'session_id': driver_chrome.session_id,
    'executor_url': driver_chrome.command_executor._url
}
folder_path = 'files'
json_file_path = os.path.join(folder_path, 'webdriver_info.json')

# Check if the folder exists, and create it if not
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
try:
    with open(json_file_path, 'w') as file:
        json.dump(driver_info, file)
        print("written to file: " + json_file_path)
except Exception as e:
    print(f"An error occurred while writing the file: {e}")

print("Browser started with debugging port. You can now reuse this session.")
