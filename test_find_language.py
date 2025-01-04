from textblob.sentiments import NaiveBayesAnalyzer
from textblob import TextBlob

text = "Today is a so beautiful day. Tomorrow looks like bad weather."

blob = TextBlob(text)

# Detect language
try:
    detected_language = blob.detect_language()
    print("Detected Language:", detected_language)
except Exception as e:
    print("Error in detecting language:", e)

text = "Bonjour, comment ça va?"
blob = TextBlob(text)

print(dir(blob))  # List all methods available in TextBlob

from langdetect import detect, detect_langs

text = "Merhaba, nasılsınız?"

# Detect language
detected_language = detect(text)
print("Detected Language:", detected_language)

# Detect possible languages with probabilities
possible_languages = detect_langs(text)
print("Possible Languages:", possible_languages)
