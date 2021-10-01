import pandas as pd

#Leyendo los datos
training_data = pd.read_csv('../Datos/train.csv')
#Explorando los datos
print(training_data.head())
print(training_data.info())