import openai
import json
from dotenv import dotenv_values

config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]


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
    print(playlist)

get_playlist("romantic songs", 3) 