from model import Model
from view import View
from controller import Controller
import tkinter as tk
from feature_engineering import FeatureEngineer

if __name__ == "__main__":
    

    model = Model()
    view = View()
    controller = Controller( view=view)
    view.controller = controller
    view.create_widgets()
    view.mainloop()