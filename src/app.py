# K-means Project Tutorial

# se importan librerías
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import seaborn as sns

# cargo datos
df_raw = pd.read_csv('https://raw.githubusercontent.com/4GeeksAcademy/k-means-project-tutorial/main/housing.csv')

# guardo el dataset original
df_raw.to_csv('data/raw/datos_originales.csv', index = False)

# se crea nuevo data frame sólo con columnas de interés
df = df_raw[['Latitude', 'Longitude', 'MedInc']]

# ajusto modelo K-mean al dataset
clus = KMeans(n_clusters = 6, random_state = 308)
clus.fit(df)

# predicción de todo el dataset
pred = clus.predict(df)

# creo variable cluster
df['cluster'] = pd.Categorical(pred)

# guardo el dataset con el cluster
df.to_csv('data/processed/datos_finales.csv', index = False)