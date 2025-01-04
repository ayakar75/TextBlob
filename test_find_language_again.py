from textblob.sentiments import NaiveBayesAnalyzer
from textblob import TextBlob
from langdetect import detect, detect_langs

# TextBlob for sentiment analysis
text = "Today is a so beautiful day. Tomorrow looks like bad weather."
blob = TextBlob(text)

print("Sentiment (Polarity):", blob.sentiment.polarity)
print("Sentiment (Subjectivity):", blob.sentiment.subjectivity)

# Langdetect for language detection
text = "Merhaba, nasılsınız?"
detected_language = detect(text)
print("Detected Language:", detected_language)

possible_languages = detect_langs(text)
print("Possible Languages:", possible_languages)
