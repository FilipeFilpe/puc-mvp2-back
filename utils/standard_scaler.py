import pathlib

import pandas as pd
from sklearn.preprocessing import StandardScaler


def create_standard_scaler_to_standardization(X_input):
  # URL do dataset
  url = "https://gist.githubusercontent.com/FilipeFilpe/e8fa5d23d6fce79f435759c76fe4665d/raw/cc6a3af7623341fbc1aa74f61eddbc9f41880905/vertebral-column.csv"
  # Local dataset
  path_dataset = pathlib.Path('./database/vertebral-column.csv').absolute()
  
  array = load_dataset(path_dataset)
  X = array[:,0:6]

  scaler = StandardScaler().fit(X)

  # Padronização nos dados de entrada usando o scaler utilizado em X
  return scaler.transform(X_input)

def load_dataset(url, delimiter = ','):
  # Lê o arquivo
  dataset = pd.read_csv(url, delimiter=delimiter)
  return dataset.values