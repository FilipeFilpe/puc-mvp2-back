import pickle

import numpy as np
from utils import create_standard_scaler_to_standardization


class ModelML():
  def __init__(self, model_url:str):
    self.model_url = model_url

  # Importação do arquivo do modelo
  def import_model(self):
    pickle_in = open(self.model_url, 'rb')
    model = pickle.load(pickle_in)
    pickle_in.close()
    return model

  # Predição conforme os dados passados
  def predict(self, data):
    X_input = np.array([data[0], data[1], data[2], data[3], data[4], data[5]])
  
    rescaledEntradaX = create_standard_scaler_to_standardization(X_input.reshape(1, -1))
    model = self.import_model()
    return model.predict(rescaledEntradaX)

    