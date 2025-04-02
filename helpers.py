# here i put helper funcions (text parsers ...)
import re

def clean_lyrics(lyrics):
    clean_lyrics = re.sub(r'^.*?(?=\[)', '', lyrics, flags=re.DOTALL)
    clean_lyrics = clean_lyrics.strip()
    return clean_lyrics
