import numpy as np
from endjinn.ml.policy import FFPolicy


def test_set_weights_small():
    ff_pol = FFPolicy(10, 5)
    weights = np.random.rand(ff_pol.total_params)
    ff_pol.set_model_weights(weights)
    newly_set_weights = ff_pol.get_model_weights_as_1d()

    # Using allclose because Keras does some minor rounding on returned weights
    assert np.allclose(weights, newly_set_weights)


def test_set_weights_tiny():
    ff_pol = FFPolicy(3, 1)
    weights = np.random.rand(ff_pol.total_params)
    ff_pol.set_model_weights(weights)
    newly_set_weights = ff_pol.get_model_weights_as_1d()

    # Using allclose because Keras does some minor rounding on returned weights
    assert np.allclose(weights, newly_set_weights)
