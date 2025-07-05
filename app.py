from flask import Flask, render_template, request, jsonify
import lyricsgenius
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

from dotenv import load_dotenv
import os


from helpers import clean_lyrics, analyze_lyrics_detailed
load_dotenv()

GENIUS_API_KEY = os.getenv('GENIUS_API_KEY')

nltk.download('vader_lexicon')

app = Flask(__name__)
genius = lyricsgenius.Genius(GENIUS_API_KEY)
sia = SentimentIntensityAnalyzer()

def get_lyrics(song_title):
    try:
        song = genius.search_song(song_title)
        return song.lyrics if song else None
    except Exception:
        return None

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        song_title = request.form.get("song", "").strip()
        lyrics = get_lyrics(song_title)
        
        if lyrics:
            # Use the new detailed analysis
            detailed_analysis = analyze_lyrics_detailed(lyrics, sia)
            
            result = {
                "song": song_title,
                "lyrics": clean_lyrics(lyrics),
                "colored_lyrics": detailed_analysis['colored_lyrics'],
                "overall_mood": "Positive" if detailed_analysis['overall_sentiment']["compound"] > 0 else "Negative",
                "overall_score": detailed_analysis['overall_sentiment'],
                "sections": detailed_analysis['sections'],
                "found": True
            }
        else:
            result = {
                "song": song_title,
                "found": False,
                "error": "Song not found or lyrics unavailable"
            }
        
        return jsonify(result)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
