import argparse
import subprocess
import os

def execute_command_for_channels(file_path, base_result_dir):
    """
    Reads each line from the specified file and executes a command for each line.
    
    Args:
    - file_path: The path to the file containing one URL per line.
    - results_dir: The directory where the results should be saved.
    """
    with open(file_path, 'r') as file:
        for line in file:
            results_dir = os.path.join(base_result_dir, "transcript")  # Update this to your desired results directory
            channel_url = line.strip()  # Remove any leading/trailing whitespace
            results_dir = results_dir +"_"+ channel_url
            if channel_url:  # Check if the line is not empty
                # Construct the command with the current channel URL and results directory
                command = f"python ytb_scraper.py --channel_name \"{channel_url}\" --results_dir \"{results_dir}\""
                print(f"Executing: {command}")  # Printing the command to be executed for demonstration
                # Use subprocess to execute the command (commented out, as it can't be run here)
                subprocess.run(command, shell=True)

# Example usage
# file_path = "Channels.txt"  # Update this to the path of your file
if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--channels_list",
        help="The name of the file containing the channel list.",
        type=str,
        default="Channels.txt",
        )
    parser.add_argument(
        "--results_dir",
        help="The directory to save the transcripts.",
        type=str,
        default="transcripts",
        )
    
    args = parser.parse_args()
    file_path = args.channels_list
    results_dir = args.results_dir
    execute_command_for_channels(file_path, results_dir)
