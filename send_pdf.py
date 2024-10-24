from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
import time
from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, TimeoutException, WebDriverException

desired_port = 9222  

# Set up Chrome options to connect to the existing debugging session
chrome_options = ChromeOptions()
chrome_options.add_experimental_option("debuggerAddress", f"localhost:{desired_port}")

# Attach to the existing Chrome browser instance running in debugging mode
driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get("https://web.whatsapp.com")  # Connect to the WhatsApp Web session already logged in
    print("Reconnected to the existing session successfully.")
    print("Current Page Title: ", driver.title)
    time.sleep(5) 
except Exception as e:
    print(f"Failed to reconnect: {e}")

# Function to send a message with a file attachment to a specific contact
def send_message(contact, send_filepath):
    try:
    
        try:
            search_button = driver.find_element(By.XPATH, '//button[@aria-label="Search or start new chat"]')
            sleep(15)
            search_button.click()
        except NoSuchElementException:
            print("Search button not found.")
            return

        # Locate the search input box and enter the contact's name
        try:
            search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@role="textbox"]')
            search_box.send_keys(contact)
            sleep(2)  # Wait for search results to load
        except NoSuchElementException:
            print("Search bar not found.")
            return

        # Click the contact's name in the search results
        try:
            contact_click = driver.find_element(By.XPATH, f'//span[@title="{contact}"]')
            sleep(5)
            contact_click.click()
        except (NoSuchElementException, KeyError):
            print(f"Contact '{contact}' not found.")
            return

        # Click the attach button to attach a file
        try:
            attach = driver.find_element(By.XPATH, '//div[@title="Attach"]')
            attach.click()
        except NoSuchElementException:
            print("Attach button not found.")
            return

        # Find the file input element and send the file path to it
        try:
            file_click = driver.find_element(By.XPATH, '//input[@accept="*"]')
            file_click.send_keys(send_filepath)
            sleep(5)  # Give time for the file to upload
        except (NoSuchElementException, FileNotFoundError):
            print(f"File {send_filepath} not found.")
            return

        # Click the send button to send the message
        try:
            button = driver.find_element(By.XPATH, '//span[@data-icon="send"]')
            button.click()
            sleep(15)  # Wait for the message to be sent
        except NoSuchElementException:
            print("Send button not found.")
            return

    # Handle other interaction-related exceptions
    except (ElementNotInteractableException, TimeoutException, WebDriverException) as e:
        print("An unexpected error occurred: ", e)
        return

    return 1  # Return success if the message was sent

# Function to read contact-filepath pairs from a file and send the message
def input_file(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()  
                temp = line.split('|', 1)  
                contact = temp[0]
                send_filepath = temp[1]
                status = send_message(contact, send_filepath)
                if status == 1:
                    print(f"The message is sent to {contact}")
                else:
                    return 0  
                sleep(5)
            print("The file is sent to all contacts.")

    # Handle various file-related exceptions
    except IsADirectoryError:
        print(f"Error: The path {file_path} is a directory, not a file.")
        return
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return
    except IndexError:
        print("Error: A line in the file doesn't follow the correct format (contact|filepath).")
        return
    except PermissionError:
        print(f"Error: You don't have permission to read the file {file_path}.")
        return

# Call the function with the path to the file containing contact|filepath pairs
input_file("files//info_new.txt")
#Can even close the driver if we don't have to send pdf file again. Else can keep it running adn overwrite the info_new_ex.txt with new contacts and run it again.
#Uncommend the below line based on the need.
#driver.close() 