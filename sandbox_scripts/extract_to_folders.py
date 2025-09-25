import os
import zipfile

def extract_and_rename():
    print("extract_and_rename")
    current_dir = os.getcwd()
    for filename in os.listdir(current_dir):
        if filename.lower().endswith('.zip'):
            zip_path = os.path.join(current_dir, filename)
            folder_name = os.path.splitext(filename)[0]
            extract_path = os.path.join(current_dir, folder_name)

            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(extract_path)

            print(f'Extracted and renamed folder: {folder_name}')

if __name__ == "__main__":
    extract_and_rename()

print( "hello world")
extract_and_rename()
