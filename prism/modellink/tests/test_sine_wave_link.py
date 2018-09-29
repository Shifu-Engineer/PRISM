# -*- coding: utf-8 -*-

# %% IMPORTS
from __future__ import absolute_import, division, print_function

# Built-in imports
from os import path

# Package imports
import numpy as np

# PRISM imports
from prism._internal import check_instance
from prism.modellink import ModelLink, SineWaveLink

# Save the path to this directory
dirpath = path.dirname(__file__)


# %% PYTEST CLASSES AND FUNCTIONS
# Pytest for SineWaveLink class
def test_SineWaveLink():
    # Save paths to data file
    model_data = path.join(dirpath, 'data/data_sine_wave.txt')

    # Initialize SineWaveLink class
    model_link = SineWaveLink(model_data=model_data)

    # Check if this instance is from a proper ModelLink subclass
    assert check_instance(model_link, ModelLink)

    # Call model
    par_set = [4, 3, 5, 4.6]
    par_dict = dict(zip(model_link._par_name, np.array(par_set)))
    exp_mod_out = [3.9477019656331063, 4.268437351642151, 4.204589086020441,
                   3.8476310228828132, 3.7089682798878445]
    assert np.isclose(model_link.call_model(1, par_dict, model_link._data_idx),
                      exp_mod_out).all()

    # Retrieve model discrepancy variance
    assert np.isclose(model_link.get_md_var(1, model_link._data_idx),
                      [0.01, 0.01, 0.01, 0.01, 0.01]).all()
