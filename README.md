## Introduction

This repository contains a Python script that allows you to fetch video transcripts from a YouTube channel.

## Installation

1. Clone the repository to your local machine using the following command:

   ```
   git clone https://github.com/imomayiz/youtube_scraper.git
   ```

2. Navigate to the `youtube_scraper` directory:

3. Install the necessary dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the `youtube_scraper` directory and add your YouTube API key. The `.env` file should contain the following line:

   ```
   YOUTUBE_API_KEY=your-api-key
   ```

   Replace `your-api-key` with your actual YouTube API key. For more details on how to create a youtube api key, follow this [guide](https://medium.com/@momayiz.imane/scraping-youtube-video-transcripts-5e3edee5656b).

## Usage

To fetch video transcripts from a YouTube channel, follow these steps:

1. Open a terminal or command prompt.

2. Navigate to the `youtube_scraper` directory:

   ```
   cd youtube_scraper
   ```

3. Run the following command to execute the script:

   ```
   python ytb_scraper.py --channel_name "your-channel-name" --results_dir "path-to-save-transcripts" --max_videos 10
   ```

   Replace `your-channel-name` with the name of the YouTube channel you want to fetch transcripts from. Replace `path-to-save-transcripts` with the directory where you want to save the transcripts. The `--max_videos` argument is optional and allows you to limit the number of videos to fetch a transcript for.

4. The script will start fetching the transcripts from all videos in the specified channel and save them in separate text files.

### Automated use

1. create a `.txt` file with a channel name in each line

   example :
   channel1
   channel2
   channel3

2. Run the following command to execute the script:

   ```
   python execute.py --channels_list "your-channel-list" --results_dir "path-to-save-transcripts"
   ```

   Replace `your-channel-name` with the name of the file with the YouTube channels names you want to fetch transcripts from (with the default file being named `Channels.txt`). Replace `path-to-save-transcripts` with the directory where you want to save the transcripts (with the default directory being the current directory!).

3. The script will start fetching the transcripts from all videos in the specified channel and save them in separate folders.

   **N.B.** Not all videos have a transcript!

### Automated File Cleanup Process

Automate the cleanup of text files in a directory with this script. Here's how to use it:

1. **Open Terminal:** Navigate to the script's directory.

```

cd path-to-your-script-directory

```

2. **Execute Script:** Run the script with options.

```

python script_name.py --delete_files True --create_backup True --backup_folder "Deleted_files"

```

- `script_name.py`: Replace with your script's filename.
- `--delete_files True`: Enable file deletion.
- `--create_backup True`: Enable backup creation.
- `--backup_folder "Deleted_files"`: Set backup directory.

3. **Operation:** The script processes `.txt` files within 'transcript' folders, evaluating them against criteria like keyword presence or word count. Matching files are backed up and deleted.

4. **Feedback:** Progress and actions (backup and deletion) are shown in the terminal.

**Note:** Customize script arguments to fit your cleanup requirements.

```

```
