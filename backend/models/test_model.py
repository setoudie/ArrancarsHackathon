from backend.utils import wrangle, translate_text
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

def categorize_sentiments(results):
    """
    Catégorise les sentiments en fonction des labels et scores.

    Args:
        results (list): Liste des résultats contenant 'label' et 'score'.

    Returns:
        list: Liste des catégories ('negative', 'neutral', 'positive').
    """
    categories = []
    for result in results:
        label = result['label']
        score = result['score']

        if label == "LABEL_0" and 0 <= score <= 0.40:
            categories.append("negative")
        elif (label == "LABEL_0" or label == "LABEL_1") and 0.40 < score <= 0.60:
            categories.append("neutral")
        elif label == "LABEL_1" and 0.60 < score <= 1:
            categories.append("positive")
        else:
            categories.append("unknown")  # Cas non prévu (optionnel)

    return categories


for i, (text, result) in enumerate(zip(text, results), start=1):
    print(f"**Avis {i}**")
    print(f"Description: {text}")
    print(f"Label: {result['label']}")
    print(f"Score: {result['score']:.2f}")
    print("-" * 400)

