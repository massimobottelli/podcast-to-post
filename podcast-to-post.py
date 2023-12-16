# input: URL of a podcast RSS feed
# parse feed, show episodes, select episodes, download audio file
# use OpenAI Whisper to transcript the audio
# publish the text as blog post

import feedparser
import ssl
from prettytable import PrettyTable
from datetime import datetime
import requests

def divider():
    print("-" * 40)

def format_date(date_str):
    """
    Format the date string in the format "%a, %d %b %Y %H:%M:%S %z" to "%d/%m/%Y".
    Parameters: date_str (str): The input date string to be formatted.
    Returns: str: The formatted date string or the original string if parsing fails.
    """
    try:
        # Attempt to parse the input date string and format it
        date_obj = datetime.strptime(date_str, "%a, %d %b %Y %H:%M:%S %z")
        return date_obj.strftime("%d/%m/%Y")
    except ValueError:
        # Return the original date string if parsing fails
        return date_str

def extract_mp3_url(feed_url):
    """
        Extract MP3 URLs from a podcast feed.
        Parameters: feed_url (str): The URL of the podcast feed.
        Returns: list: A list of MP3 URLs extracted from the feed entries.
        """
    # Parse the podcast feed from the specified URL
    feed = feedparser.parse(feed_url)

    # Initialize a list to store extracted MP3 URLs
    mp3_urls = []

    # Iterate through entries in the feed
    for entry in feed.entries:

        # Check if 'enclosures' key is present in the entry
        if 'enclosures' in entry:

            # Iterate through enclosures in the entry
            for enclosure in entry.enclosures:

                # Check if 'href' key is present in the enclosure
                if 'href' in enclosure:

                    # Retrieve and append the MP3 URL to the list
                    mp3_url = enclosure.href
                    mp3_urls.append(mp3_url)

    # Return the list of extracted MP3 URLs
    return mp3_urls


# Main

# Allow unverified SSL certificate
if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context

# Collect podcast RSS feed from user
url = input("Enter the URL (or press Enter to use the default): ").strip()
url = url or 'http://www.spreaker.com/show/2130193/episodes/feed'


try:
    # Attempt to parse the RSS feed from the specified URL
    feed = feedparser.parse(url)

    # Extract podcast author
    podcast_author = feed.feed.get('author', 'Unknown Author')

    # Extract podcast title
    podcast_title = feed.feed.get('title', 'Unknown Title')

    print()
    print(f"Title: {podcast_title}")
    print(f"Author: {podcast_author}")

    # Create a PrettyTable to display the feed entries
    table = PrettyTable()
    table.field_names = ["ID", "Date", "Title"]
    table.align = "l"  # Set text alignment to left

    # Iterate through the entries in the parsed feed
    for i, entry in reversed(list(enumerate(feed.entries))):

        # Format the date of the entry
        formatted_date = format_date(entry.published)

        # Truncate the title if it exceeds 50 characters
        truncated_title = entry.title[:50] + "..." if len(entry.title) > 50 else entry.title

        # Add a row to the PrettyTable for each entry
        table.add_row([i + 1, formatted_date, truncated_title])

    print(table)
    divider()

    # Collect the selected item from user
    selected_id = input("Enter the ID of the item you want to download (or press Enter for latest): ").strip()
    selected_id = selected_id or 1
    if selected_id:
        # Convert selected_id to an integer
        selected_id = int(selected_id)

        # Check if the selected_id is within the valid range of entries
        if 1 <= selected_id <= len(feed.entries):

            # Retrieve the selected entry from the feed
            selected_entry = feed.entries[selected_id - 1]

            # Extract MP3 URLs from the feed
            mp3_urls = extract_mp3_url(url)

            # Check if there are MP3 URLs in the feed
            if mp3_urls:
                # Retrieve the MP3 URL corresponding to the selected entry
                selected_mp3_url = mp3_urls[selected_id - 1]
                divider()
                print(f"Downloading MP3 content from: {selected_mp3_url}")

                # Download content using requests
                response = requests.get(selected_mp3_url)

                # Check if the request was successful (status code 200)
                if response.status_code == 200:
                    # Save the content to a file
                    filename = f"{podcast_title} - {selected_entry.title}.mp3"  # Example: Use the first 20 characters of the title as the filename
                    with open(filename, 'wb') as file:
                        file.write(response.content)

                    print(f"Download successful! MP3 file saved to {filename}")
                else:
                    print(f"Download failed with status code: {response.status_code}")

                divider()
            else:
                print("No MP3 URLs found in the feed.")
        else:
            print("Invalid ID. Exiting.")

# Handle exceptions that might occur during feed parsing
except Exception as e:
    print(f"An error occurred: {e}")
