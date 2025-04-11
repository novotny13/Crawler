import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin

class FeatureEngineer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()
        X['Věk'] = 2024 - X['První registrace']
        X['Věk'] = X['Věk'].replace(0, np.nan)

        X['Výkon/Spotřeba'] = X['Výkon'] / (X['Spotřeba'] + 1)
        X['Roční_nájezd'] = X['Najeto'] / (X['Věk'] + 1)
        X['Výkon_x_Věk'] = X['Výkon'] * X['Věk']
        X['Spotřeba^2'] = X['Spotřeba'] ** 2

        X.replace([np.inf, -np.inf], np.nan, inplace=True)
        return X
