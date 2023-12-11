import os
import shutil
import time

def list_files_in_directory(directory):
    files = []
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            files.append(file_path)
    return files

def is_file_recently_modified(file_path):
    current_time = time.time()
    file_stats = os.stat(file_path)
    modification_time = file_stats.st_mtime
    creation_time = file_stats.st_ctime
    time_diff = current_time - max(modification_time, creation_time)
    return time_diff <= 24 * 60 * 60

def update_files(files):
    for file in files:
        with open(file, 'a') as f:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            f.write(f"\nUpdated at {timestamp}")

def create_last_24hours_folder():
    folder_name = "last_24hours"
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
def move_files_to_last_24hours_folder(files):
    destination_folder = "last_24hours"
    for file in files:
        destination_path = os.path.join(destination_folder, os.path.basename(file))
        shutil.move(file, destination_path)
current_directory = os.getcwd()
files = list_files_in_directory(current_directory)
recent_files = [file for file in files if is_file_recently_modified(file)]
update_files(recent_files)
create_last_24hours_folder()
move_files_to_last_24hours_folder(recent_files)