# sentrack
Sentrack - Song Lyrics Sentiment Analysis

## Overview

Sentrack is a Flask-based web application that analyzes the sentiment of song lyrics. Users can enter a song title, and the app fetches the lyrics, processes them with sentiment analysis, and visualizes the results using a graph.

## Features

* Fetch song lyrics from the Genius API.

* Perform sentiment analysis using NLTK's VADER (Valence Aware Dictionary and sEntiment Reasoner).

* Display the lyrics and sentiment analysis results side by side.

* Interactive visualization of sentiment scores.

### Technologies Used

- Backend: Flask, Python

- Frontend: HTML, CSS, JavaScript (Chart.js for visualization)

- APIs: Genius API for lyrics fetching

- Sentiment Analysis: NLTK VADER

### Installation

#### Prerequisites

1. You can install the required dependencies using:
`
pip install -r requirements.txt
`

2. Setting Up Genius API Key

3. Create a .env file in the root directory and add:
`
GENIUS_API_KEY=your_api_key_here
`
4. Running the Application

5. Start the Flask server with:
`
python app.py
`
6. The application will be available at http://127.0.0.1:5000/.

### Usage

- Enter the song title in the search bar.

- The app will fetch lyrics from Genius.

- Sentiment analysis will be performed.

- Results will be displayed with the lyrics on the left and a graph on the right.

