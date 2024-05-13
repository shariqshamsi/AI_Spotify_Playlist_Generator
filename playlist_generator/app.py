import spotipy
from dotenv import dotenv_values
import openai
import json
import argparse


config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]

parser = argparse.ArgumentParser(description = "Simple command line utility")
parser.add_argument("-p", type=str, help="The prompt to describe the playlist")
parser.add_argument("-n", type=int, default=8, help="The number of songs add to playlist")

args = parser.parse_args()



def get_playlist(prompt, count=5):
    example_json = """
    [
        {"song": "Someone Like You", "artist": "Adele"},
        {"song": "Hurt", "artist": "Johnny Cash"},
        {"song": "Tears in Heaven", "artist": "Eric Clapton"},
        {"song": "Back to December", "artist": "Taylor Swift"},
        {"song": "Everybody Hurts", "artist": "R.E.M."}
    ]
    """

    messages = [
        {"role":"system", "content": """You are a helpful playlist generating assistant.
        You should generate a list of songs and their artist according to a text prompt.
        You should return a JSON array, where each element follows this format:
        {"song":<song_title>, "artist":<artist_name>}"""},
        
        {"role":"user","content":"Generate a playlist of 5 songs based on this prompt: super super sad songs"},
        {"role":"assistant", "content": example_json},
        {"role":"user","content":f"Generate a playlist of {count} songs based on this prompt: {prompt}"},
    ]

    res = openai.chat.completions.create(
        messages = messages,
        model= "gpt-3.5-turbo",
        max_tokens=400
        
    )

    playlist = json.loads(res.choices[0].message.content)
    return playlist

playlist = get_playlist(args.p,args.n)
print(playlist)


sp = spotipy.Spotify(
    auth_manager=spotipy.SpotifyOAuth(
        client_id= config["SPOTIFY_CLIENT_ID"],
        client_secret= config["SPOTIFY_CLIENT_SECRET"],
        redirect_uri="http://localhost:9999",
        scope= "playlist-modify-private"
    )
)

current_user = sp.current_user()

track_ids = []
assert current_user is not None

for item in playlist:
    artist, song = item["artist"], item["song"]
    query = f"{song} {artist}"
    search_results = sp.search(q=query, type="track",limit=10)
    track_ids.append(search_results["tracks"]["items"][0]["id"])
    

created_playlist = sp.user_playlist_create(
    current_user["id"],
    public=False,
    name= args.p
)

sp.user_playlist_add_tracks(current_user["id"], created_playlist["id"], track_ids )