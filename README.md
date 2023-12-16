# Podcast to Post

This Python script allows you to parse a podcast RSS feed, view episodes, select specific episodes, and download their audio files. Additionally, it uses OpenAI Whisper to transcribe the downloaded audio content and publishes the transcript as a blog post.

## Features

- Parse and display information from a podcast RSS feed.
- Select and download specific episodes.
- Use OpenAI Whisper for audio transcription.
- Publish transcriptions as blog posts.

## Requirements

- Python 3.x
- Dependencies (install using `pip install -r requirements.txt`):
  - `feedparser`
  - `prettytable`
  - `requests`

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/massimobottelli/podcast-to-post.git

Navigate to the project directory:
 cd podcast-rss-downloader

Run the script:
 python podcast-to-post.py

Follow the prompts to enter the podcast RSS feed URL, select episodes, and download audio files.
