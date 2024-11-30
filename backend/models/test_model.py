from sentence_transformers import SentenceTransformer
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt

# 1. Charger les descriptions
descriptions = [
    "My lovely Pat has one of the GREAT voices of her generation. I have listened to this CD for YEARS and I still LOVE IT. ...",
    "Despite the fact that I have only played a small portion of the game, the music I heard ...",
    "I bought this charger in Jul 2003 and it worked OK for a while. ...",
    "Check out Maha Energy's website. Their Powerex MH-C204F charger works ...",
    "Reviewed quite a bit of the combo players and was hesitant ...",
    "I also began having the incorrect disc problems that I've read about on here. ...",
    "I love the style of this, but after a couple years, the DVD is giving me problems. ...",
    "I cannot scroll through a DVD menu that is set up vertically. ...",
    "Exotic tales of the Orient from the 1930's. 'Dr Shen Fu', a Weird Tales magazine reprint, is about ...",
    "Firstly, I enjoyed the format and tone of the book (how the author addressed the reader). ..."
]

# 2. Convertir les textes en embeddings avec Sentence-BERT
model = SentenceTransformer('all-MiniLM-L6-v2')  # Modèle léger pour embeddings
embeddings = model.encode(descriptions)

# 3. Clustering hiérarchique (Agglomerative Clustering)
clustering = AgglomerativeClustering(n_clusters=None, distance_threshold=1.5, affinity='euclidean', linkage='ward')
labels = clustering.fit_predict(embeddings)

# 4. Visualisation du dendrogramme pour ajuster le seuil de distance
linked = linkage(embeddings, method='ward')

plt.figure(figsize=(10, 7))
dendrogram(linked, orientation='top', labels=[f"Doc {i}" for i in range(len(descriptions))], distance_sort='descending', show_leaf_counts=True)
plt.title("Dendrogram - Hierarchical Clustering")
plt.show()

# 5. Afficher les résultats
clusters = {i: [] for i in range(max(labels) + 1)}
for i, label in enumerate(labels):
    clusters[label].append(descriptions[i])

print("Résultats du clustering :")
for cluster_id, docs in clusters.items():
    print(f"Cluster {cluster_id}:")
    for doc in docs:
        print(f"  - {doc[:100]}...")  # Affiche un extrait de chaque document
