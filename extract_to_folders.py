import os
import zipfile
import sys
import shutil


def extract_and_organize(directory):
    for filename in os.listdir(directory):
        if filename.lower().endswith('.zip'):
            zip_path = os.path.join(directory, filename)
            folder_name = os.path.splitext(filename)[0]
            extract_path = os.path.join(directory, folder_name)
            print(extract_path)

            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(extract_path)

            print(f'Extracted and renamed folder: {folder_name}')
            os.remove(zip_path)


dir_to_use = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
extract_and_organize(dir_to_use)

