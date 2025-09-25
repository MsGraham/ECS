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

            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(directory)

            # # Check what was extracted
            extracted_items = [item for item in os.listdir(directory) if not item.endswith('.zip')]

            # Determine if extracted content is a single folder named as folder_name
            # or multiple files/folders
            if len(extracted_items) == 1 and extracted_items[0] == folder_name and os.path.isdir(os.path.join(directory, extracted_items[0])):
                # Already extracted into a single folder named after the zip
                final_folder_path = os.path.join(directory, extracted_items[0])
                print(f'Extracted {filename} to folder {final_folder_path} and deleted the zip file.')
            # else:
                # Create the folder if it doesn't exist
                # if not os.path.exists(extract_path):
                #     os.mkdir(extract_path)
                # Move extracted items into the new folder
                # for item in extracted_items:
                #     src = os.path.join(directory, item)
                #     dst = os.path.join(extract_path, item)
                #     shutil.move(src, dst)
                # final_folder_path = extract_path
                # print(f'Extracted {filename} to folder {final_folder_path} and deleted the zip file.')

            # Delete the original zip file
            # os.remove(zip_path)


if __name__ == "__main__":
    dir_to_use = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()


print( "hello world")
# mb_path = os.path("mb.zip")
# os.remove(mb_path)
# extract_and_rename()
dir_to_use = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
extract_and_organize(dir_to_use)
# extract_and_rename(dir_to_use)
