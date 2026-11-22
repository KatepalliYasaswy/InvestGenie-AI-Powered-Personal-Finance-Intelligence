import shap
import pandas as pd

def explain_prediction(model, data):

    explainer = shap.TreeExplainer(model)

    shap_values = explainer.shap_values(data)

    return shap_values