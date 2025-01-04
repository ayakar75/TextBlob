from textblob.sentiments import NaiveBayesAnalyzer
from textblob import TextBlob

text = "Today is a so beautiful day. Tomorrow looks like bad weather."

blob = TextBlob(text)



print("Detect Language:", blob.detect_language())