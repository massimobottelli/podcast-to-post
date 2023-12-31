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
  - `openai-whisper`

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/massimobottelli/podcast-to-post.git

2. Navigate to the project directory:
 cd podcast-rss-downloader

3. Run the script:
 python podcast-to-post.py

4. Follow the prompts to enter the podcast RSS feed URL, select episodes, and download audio files.

## Backlog

- create a blog post with transcription
- create an index of posts
