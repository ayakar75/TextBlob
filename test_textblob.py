from textblob import TextBlob

text = "Today is a so beautiful day. Tomorrow looks like bad weather."

blob = TextBlob(text)

# Analiz sonuçları
print("Sentences:", blob.sentences)  # Cümleler
print("Words:", blob.words)          # Kelimeler
print("Sentiment:", blob.sentiment)  # Duygu analizi
print("Tags:", blob.tags)

#for word, pos in blob.tags:
    #print(f"{word}: {pos}")

print("Noun Phrases:", blob.noun_phrases)

