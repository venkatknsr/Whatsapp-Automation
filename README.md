# WhatsApp Web Automation

This repository contains Python scripts for automating interactions with WhatsApp Web using Selenium. The scripts allow you to start a session, send messages with file attachments, and manage session data. 

## Usage Instructions

1. Modify the `info_new.txt` in the `files` folder with the contacts you wish to send files to, including the file path of the file to be sent.
2. Add the corresponding file to the `files` folder.

### Important Note
After running `invoke.py`, press `Ctrl + C` to stop the script before running `send_pdf.py`, or alternatively, open a new terminal window (for example, when using VSCode) to execute `send_pdf.py`.

## Requirements

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your machine.
- Google Chrome installed and the corresponding ChromeDriver.
- Install the necessary Python packages:

```bash
pip install selenium
