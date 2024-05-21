import os
import zipfile

def extract_all_zips(directory):
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if item.endswith('.zip'):
            with zipfile.ZipFile(item_path, 'r') as zip_ref:
                # Extract into a folder with the same name as the zip file (without the extension)
                # extract_path = os.path.join(directory, os.path.splitext(item)[0])
                # os.makedirs(extract_path, exist_ok=True)
                
                # extract directly on the path
                zip_ref.extractall(directory)
                print(f'Extracted {item} to {directory}')

# Specify the directory containing the zipped folders
urfd_directory = 'URFD-BALANCED/URFD-ADL'

# Extract all zipped folders in the specified directory
extract_all_zips(urfd_directory)
