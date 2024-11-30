from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


# @app.route('/classify-opinion/', methods=['POST'])
# def classify():
#     try:
#         # Charger les données depuis le fichier CSV
#         data = request.get_json()
#         file_path = data.get("file_path")
#
#         if not file_path:
#             return jsonify({"error": "File path not provided"}), 400
#
#         # Charger le fichier CSV
#         header = ['Labels', 'Title', 'Description']
#         df = pd.read_csv(file_path, names=header)
#
#         # Appeler classify_opinion
#         results = classify_opinion(df)
#
#         return jsonify({"results": results}), 200
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
@app.route('/cluster-opinions/')
def cluster_opinions():
    try:
        # Charger les données
        df = wrangle("/home/setoudie/PycharmProjects/Arrancars/backend/data/data.csv")

        # Appliquer le clustering sur les avis
        df_with_clusters = add_clusters_to_dataframe(df)

        # Convertir le DataFrame en dictionnaire pour la réponse JSON
        result = df_with_clusters.to_dict(orient="records")

        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run()
