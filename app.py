from flask import Flask, render_template, request, jsonify
import lyricsgenius
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

from dotenv import load_dotenv
import os

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
        sentiment_scores = sia.polarity_scores(lyrics)
        
        result = {
            "song": song_title,
            "lyrics": lyrics,
            "mood": "Positive" if sentiment_scores["compound"] > 0 else "Negative",
            "score": sentiment_scores
        }
        return jsonify(result)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
