from backend.utils import *
from transformers import pipeline

# Initialize the pipeline for text classification
pipe = pipeline("text-classification", model="phanerozoic/BERT-Sentiment-Classifier")

# Example input texts for classification
"""texts = [
    "le colis n'est pas arrive a l'heure prevue",
    "le produit est excellent, je le recommande",
    "j'ai eu une mauvaise expérience avec ce service"
]"""
df = wrangle("/home/setoudie/PycharmProjects/Arrancars/backend/data/data.csv")

text = list(df["Description"].head(10))



# Perform the classification with multiple texts
show = df["Description"].head(10)

results = pipe(text)



for i, (text, result) in enumerate(zip(text, results), start=1):
    print(f"**Avis {i}**")
    print(f"Description: {text}")
    print(f"Label: {result['label']}")
    print(f"Score: {result['score']:.2f}")
    print("-" * 400)

print(classify_opinion(df))

