# WhatsApp Web Automation

This repository contains Python scripts designed for automating interactions with WhatsApp Web using Selenium. The provided scripts facilitate the initiation of a session, sending messages with file attachments, and managing session data effectively.

## Usage Instructions

### File Preparation
To use this automation tool, you need to modify the `info_new.txt` file located in the `files` folder. Add the contacts you wish to send files to, along with the corresponding file paths for the files you intend to send. Ensure that the file paths are correctly specified and that the files are present in the designated locations.

### Requirements

Before you begin, please ensure that you meet the following prerequisites:

- **Python 3.x**: Make sure Python is installed on your machine.
- **Google Chrome**: Install the latest version of Google Chrome.
- **ChromeDriver**: Ensure that the ChromeDriver compatible with your version of Chrome is installed and available in your system's PATH.
- **Python Packages**: Install the required Python packages by running the following command:

```bash
pip install selenium
