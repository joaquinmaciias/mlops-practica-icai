import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df["target"] = iris.target
df.to_csv("data/iris_dataset.csv", index=False)
print("Archivo iris_dataset.csv creado exitosamente.")
