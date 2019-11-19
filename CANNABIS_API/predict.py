"""
Prediction on the id
"""


import pickle
import numpy as np
from .models import Records


def predict_strain(strain_id, cache=None):
    """
    determine and return 3 id for the strains similar to the one provided
    """
    id_set = pickle.dumps((strain_id))
    if cache and cache.exists(id_set):
        log_reg = pickle.loads(cache.get(id_set))
    else:
        modelfile = 'models/final_prediction.pickle'
        log_reg = pickle.loads(open(modelfile))
        cache and cache.set(id_set, pickle.dumps(log_reg))
    return log_reg.predict(id_set)[:3]


