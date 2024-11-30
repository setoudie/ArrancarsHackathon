import kagglehub
import pandas as pd
# Download latest version
# path = kagglehub.dataset_download("kritanjalijain/amazon-reviews")

path = "https://drive.google.com/file/d/1KUE_1frdPYqaoqsOUFIw_YyNahDJBAM1/view?usp=sharing"
print("Path to dataset files:", path)

df = pd.read_csv(path)
print(df.head(5))
