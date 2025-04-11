from model import Model

"""
Třída Controller propojuje modely s GUI – zajišťuje interakci mezi vstupy a výstupy.
"""

class Controller:
    def __init__(self, view):
        self.view = view
        self.model = Model()

    def handle_price_prediction(self):
        """
        Spousti predikci modelu a zobrazeni vysledku ve view.

        """
        user_input = self.view.get_form_data()
        price = self.model.predict_price(user_input)
        self.view.set_price_input(price)

    def handle_deal_prediction(self):
        """
              Spousti predikci modelu a zobrazeni vysledku ve view.

              """
        user_input = self.view.get_form_data()
        deal_score = self.model.predict_deal(user_input)
        self.view.display_deal_score(deal_score)
