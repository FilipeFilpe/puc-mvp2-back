import pathlib

import pandas as pd
from model import ModelML
from model.avaliador import Avaliador
from utils import load_dataset

avaliador = Avaliador()
# URL do dataset
url = "https://gist.githubusercontent.com/FilipeFilpe/e8fa5d23d6fce79f435759c76fe4665d/raw/cc6a3af7623341fbc1aa74f61eddbc9f41880905/vertebral-column.csv"

# Testa o modelo
def test_model():

  # Lê o arquivo
  array = load_dataset(url)
  X = array[:,0:6]
  Y = array[:,6]

  # Pega o arquivo do modelo
  path_model = pathlib.Path('./models_ML/modelo_classificador.pkl').absolute()
  model = ModelML(path_model)

  # Obtendo as métricas
  acuracia = avaliador.avaliar(model.import_model(), X, Y)
  
  # Testando as métricas
  assert acuracia >= 0.65