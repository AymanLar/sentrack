# here i put helper funcions (text parsers ...)
import re
from nltk.sentiment import SentimentIntensityAnalyzer

def clean_lyrics(lyrics):
    clean_lyrics = re.sub(r'^.*?(?=\[)', '', lyrics, flags=re.DOTALL)
    clean_lyrics = clean_lyrics.strip()
    return clean_lyrics

def parse_lyrics_sections(lyrics):
    """Parse lyrics into sections (verses, choruses, etc.)"""
    if not lyrics:
        return []
    
    # Split by common section markers
    sections = re.split(r'(\[.*?\])', lyrics)
    
    parsed_sections = []
    current_section = ""
    current_section_type = "verse"
    
    for i, section in enumerate(sections):
        if section.strip():
            # Check if this is a section header (like [Verse], [Chorus], etc.)
            if re.match(r'^\[.*?\]$', section.strip()):
                # Save previous section if it exists
                if current_section.strip():
                    parsed_sections.append({
                        'type': current_section_type,
                        'text': current_section.strip(),
                        'lines': current_section.strip().split('\n')
                    })
                
                # Start new section
                current_section_type = section.strip()[1:-1].lower()  # Remove brackets
                current_section = ""
            else:
                current_section += section + "\n"
    
    # Add the last section
    if current_section.strip():
        parsed_sections.append({
            'type': current_section_type,
            'text': current_section.strip(),
            'lines': current_section.strip().split('\n')
        })
    
    # If no sections were found, treat the whole thing as a verse
    if not parsed_sections and lyrics.strip():
        parsed_sections.append({
            'type': 'verse',
            'text': lyrics.strip(),
            'lines': lyrics.strip().split('\n')
        })
    
    return parsed_sections

def analyze_section_sentiment(section_text, sia):
    """Analyze sentiment of a specific section"""
    if not section_text or not section_text.strip():
        return {'compound': 0, 'pos': 0, 'neg': 0, 'neu': 0}
    
    scores = sia.polarity_scores(section_text)
    return scores

def get_sentiment_color(compound_score):
    """Get color based on sentiment score"""
    if compound_score >= 0.1:
        return '#4caf50'  # Green for positive
    elif compound_score <= -0.1:
        return '#ff4c4c'  # Red for negative
    else:
        return '#ffd700'  # Yellow for neutral

def analyze_lyrics_detailed(lyrics, sia):
    """Analyze lyrics with detailed sentiment breakdown by sections"""
    if not lyrics:
        return {
            'overall_sentiment': {'compound': 0, 'pos': 0, 'neg': 0, 'neu': 0},
            'sections': [],
            'colored_lyrics': ''
        }
    
    # Parse lyrics into sections
    sections = parse_lyrics_sections(lyrics)
    
    # Analyze each section
    analyzed_sections = []
    colored_lyrics_parts = []
    
    for section in sections:
        sentiment = analyze_section_sentiment(section['text'], sia)
        color = get_sentiment_color(sentiment['compound'])
        
        analyzed_section = {
            'type': section['type'],
            'text': section['text'],
            'sentiment': sentiment,
            'color': color
        }
        analyzed_sections.append(analyzed_section)
        
        # Create colored HTML for this section
        colored_text = f'<span style="background-color: {color}; padding: 2px 4px; border-radius: 3px; margin: 2px 0; display: inline-block;">{section["text"]}</span>'
        colored_lyrics_parts.append(colored_text)
    
    # Calculate overall sentiment
    overall_sentiment = analyze_section_sentiment(lyrics, sia)
    
    return {
        'overall_sentiment': overall_sentiment,
        'sections': analyzed_sections,
        'colored_lyrics': '<br><br>'.join(colored_lyrics_parts)
    }
