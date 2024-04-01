import argparse
import os
import shutil

def move_files(source_folder, destination_folder):
    # Get the list of files in the source folder
    files = os.listdir(source_folder)

    for file in files:
        # Split the file name into name and extension
        name, extension = os.path.splitext(file)

        # Extract the first part of the file name
        first_part = name.split('_')[0]

        # Create the destination folder path
        destination_path = os.path.join(destination_folder, f"transcripts_{first_part}")

        # Create the destination folder if it doesn't exist
        os.makedirs(destination_path, exist_ok=True)

        # Move the file to the destination folder
        shutil.move(os.path.join(source_folder, file), os.path.join(destination_path, file))

# Specify the source folder and destination folder
# source_folder = "Deleted_files"
# destination_folder = "./"

# Call the move_files function
if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--source_folder",
        help="Toogle deleting the files",
        type=str,
        default="Backup_folder"
    )
    
    parser.add_argument(
        "--destination_folder",
        help="Create a backup of the files.",
        type=str,
        default="./",
    )
    
    args = parser.parse_args()
    source_folder = args.source_folder
    destination_folder = args.destination_folder
    move_files(source_folder, destination_folder)