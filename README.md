# Discord Cleanup Tool

This Python script is designed to safely detect and remove specific folders associated with Discord installations that may be compromised or contain unwanted files(Token grabbers that injects into discord etc...). It specifically targets installations such as Discord, DiscordCanary, DiscordPTB, and DiscordDevelopment, focusing on directories that match known patterns indicative of modifications.

## Features

- **Process Management**: Automatically detects and terminates any active Discord processes to prevent file locking issues during the cleanup operation.
- **Targeted Folder Deletion**: Scans and removes directories deeply nested within the Discord installation paths that match criteria suggesting they contain modifications or are otherwise flagged for removal.
- **Robust Logging**: Uses the Python `logging` module to provide detailed logs of all operations, making it easy to track the actions taken by the script and any issues encountered.
- **Error Handling**: Intelligently handles common errors, such as attempts to delete folders that are in use or no longer exist, reducing unnecessary error logs and focusing on significant issues.
- **Retry Mechanism**: Implements retries for folder deletions to handle transient issues like temporary file locks or delayed release of file system resources."

## Requirements

- **Python 3.6 or higher**: Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
- **psutil library**: Required for process management. Install this library using pip:
  ```bash
  pip install psutil
  ```

## Installation

Clone the Repository: Clone this repository to your local machine using the following command:
```bash
git clone https://github.com/Dorukuz/Discord-Cleanup-Tool.git
cd discord-cleanup-tool
```

## Usage

Execute the script from the command line by running:
```bash
python clean.py
```
Ensure that you have administrative privileges if running on Windows, as terminating processes and deleting certain files may require elevated permissions.

## Configuration

No additional configuration is required to run the script as provided. However, the script currently logs all operations to the console. If you prefer logging to a file, modify the **logging.basicConfig()** call in the script to include a file name:

```Python
logging.basicConfig(filename='cleanup.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
```
