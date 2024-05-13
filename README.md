# AI_Spotify_Playlist_Generator
This repository contains a Python script for generating Spotify playlists using OpenAI and Spotify APIs.

## Usage:
Run the script python ai_play_list.py from the command line with the following options:

**-p, --playlist:** Specify the type of playlist (e.g., "fun songs", "romantic songs",  etc.) or your favorite singer name

**-n, --number:** Specify the number of songs to include in the playlist.

Run the script from the command line with options for playlist type and song count to generate and display playlists.

Example command:

**python ai_play_list.py -p "fun songs" -n 5**

This command will generate a playlist with 5 songs of the "fun songs" category and display the list in the command line. The playlist will also be created in your Spotify account with the current date and time appended to its name.

# Libraries Used :

**argparse:** For parsing command-line arguments.

**dotenv:** For loading environment variables from a .env file.

**spotipy:** A Python library for the Spotify Web API.

**logging:** For logging messages and errors.


# Note: 
The .env file containing sensitive information like API keys has been removed for security reasons. Make sure to create your own .env file with your Spotify  and openai API credentials before running the script.
