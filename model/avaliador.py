from sklearn.metrics import (accuracy_score, f1_score, precision_score,
                             recall_score)


class Avaliador:

    def avaliar(self, model, X_test, Y_test):
        """ Faz uma predição e avalia o modelo.
        """
        predicts = model.predict(X_test)
        
        return (accuracy_score(Y_test, predicts))