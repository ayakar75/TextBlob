from textblob.sentiments import NaiveBayesAnalyzer
from textblob import TextBlob

text = "Today is a so beautiful day. Tomorrow looks like bad weather."

blob = TextBlob(text)

blob = TextBlob(text, analyzer=NaiveBayesAnalyzer())

print("Naive Bayes:", blob.sentiment)

for sentence in blob.sentences:
    print(sentence.sentiment)