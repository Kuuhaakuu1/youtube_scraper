import os
import shutil
import argparse
from tqdm import tqdm

def any_threshold(iterable, threshold, condition):
    count = 0
    for item in iterable:
        if condition(item):
            count += 1
            if count >= threshold:
                return True
    return False
   
if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--delete_files",
        help="Toogle deleting the files",
        type=bool,
        default=True
    )
    parser.add_argument(
        "--create_backup",
        help="Create a backup of the files.",
        type=bool,
        default=True,
    )
    parser.add_argument(
        "--backup_folder",
        help="The directory to save the backups.",
        type=str,
        default="Deleted_files",
    )
    
    
    args = parser.parse_args()
    delete_files = args.delete_files
    create_backup = args.create_backup
    backup_folder = args.backup_folder
    
    
    folder_path = './'  # Replace with the actual parent folder path
    listofwords = ["[موسيقى]", "[ضجيج]", "[تصفيق]", "[ضحك]", "[تفجير]", "[صراخ]", "[هتاف]","‏"]
    # Iterate through folders in the parent folder
    for foldername in tqdm(os.listdir(folder_path)):
        print(f"Processing {foldername}")
        print(f"Processing {foldername} {os.path.isdir(os.path.join(folder_path, foldername))}")
        if foldername.startswith('transcript') and os.path.isdir(os.path.join(folder_path, foldername)):
            folder_paths = os.path.join(folder_path, foldername)
            
            # Iterate through files in the folder
            for filename in os.listdir(folder_paths):
                if filename.endswith('.txt'):
                    file_path = os.path.join(folder_paths, filename)
                    delete = False
                    # Check if the file meets the criteria
                    with open(file_path, 'r', encoding='utf-8') as file:
                        lines = file.readlines()
                        words = [word for line in lines for word in line.split()]
                        threshold = len(words) * 0.1
                        if len(lines) <= 10 or any_threshold(words, threshold, lambda x: x in listofwords) or True:
                            # Create a folder for deleted files if it doesn't exist
                            if create_backup:
                                deleted_files_folder = os.path.join('./', backup_folder)
                                os.makedirs(deleted_files_folder, exist_ok=True)
                                
                                # Copy the file to the "Deleted files" folder
                                shutil.copy2(file_path, deleted_files_folder)
                                
                                print(f"Moved file: {file_path} to {deleted_files_folder}")
                            delete = True
                    if delete and delete_files:
                        # Remove the original file
                        os.remove(file_path)
                        print(f"Deleted file: {file_path}")
                        
                        