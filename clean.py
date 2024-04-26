import os
import shutil
import logging
import psutil
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def terminate_discord_processes():
    """ Terminate any running Discord processes to free up file locks. """
    for proc in psutil.process_iter(['pid', 'name']):
        if 'discord' in proc.info['name'].lower():
            proc.terminate()  # or proc.kill() if terminate doesn't work
            logging.info(f"Terminated process: {proc.info['name']} with PID {proc.info['pid']}")


def find_infected_folders(base_path):
    """ Generate the list of infected folder paths to check based on a base path. """
    infected_folders = []
    folder_list = ['Discord', 'DiscordCanary', 'DiscordPTB', 'DiscordDevelopment']
    for folder_name in folder_list:
        folder_path = os.path.join(base_path, folder_name)
        if os.path.isdir(folder_path):
            for subdir, dirs, files in os.walk(folder_path):
                if 'app-' in subdir:
                    for dir in dirs:
                        if 'modules' in dir:
                            module_path = os.path.join(subdir, dir)
                            for subsubdir, subdirs, subfiles in os.walk(module_path):
                                if 'discord_desktop_core-' in subsubdir:
                                    infected_folders.append(subsubdir)
    return infected_folders

def remove_folders(folders):
    for folder in folders:
        retries = 3  # Maximum number of retries
        while retries > 0:
            try:
                if os.path.exists(folder):  # Check if the folder still exists
                    shutil.rmtree(folder)
                    logging.info(f"Removed folder: {folder}")
                    break
                else:
                    logging.warning(f"Path not found, skipping removal: {folder}")
                    break
            except Exception as e:
                error_message = str(e)
                if "The system cannot find the path specified" not in error_message:
                    logging.error(f"Failed to remove {folder}: {error_message}")
                time.sleep(1)
                retries -= 1
                if retries == 0 and "The system cannot find the path specified" not in error_message:
                    logging.error(f"Final attempt failed, could not remove {folder}")

def main():
    base_path = os.getenv('LOCALAPPDATA')
    if base_path is None:
        logging.error("LOCALAPPDATA environment variable is not set.")
        return
    terminate_discord_processes()  # Ensure no Discord processes are running
    
    infected_folders = find_infected_folders(base_path)
    remove_folders(infected_folders)
    print("Succesfilly removed infected files!")
main()