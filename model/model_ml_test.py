import pathlib

from model import ModelML

predict_data_AB = [68.83, 22.22, 50.09, 46.61, 105.99, -3.53]
predict_data_NO = [48.9, 5.59, 55.5, 43.32, 137, 19.85]

# Testa a predição do modelo conforme é feito pelo aplicação
def test_predict_model():
  path_model = pathlib.Path('./models_ML/modelo_classificador.pkl').absolute()
  model = ModelML(path_model)

  result_predict_AB = model.predict(predict_data_AB)
  result_predict_NO = model.predict(predict_data_NO)

  assert [result_predict_AB[0], result_predict_NO[0]] == ['AB', 'NO']