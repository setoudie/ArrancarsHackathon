from transformers import pipeline

# Initialize the pipeline for text classification
pipe = pipeline("text-classification", model="phanerozoic/BERT-Sentiment-Classifier")

# Example input texts for classification
texts = [
    "le colis n'est pas arrive a l'heure prevue",
    "le produit est excellent, je le recommande",
    "j'ai eu une mauvaise expérience avec ce service"
]

# Perform the classification with multiple texts
results = pipe(texts)

# Print the results
for i, result in enumerate(results):
    print(f"Text {i+1} Result:", result)
