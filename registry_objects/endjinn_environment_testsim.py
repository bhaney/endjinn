from endjinn.environment import Environment
from endjinn.state_block import Series
import numpy as np

"""
This example environment shows use of:
    - tick_update() implementation
    - Series state block for time series
    
The environment simulates a single asset price using Gaussian noise as percentage change per tick. That is, every tick
the price will change by +/- 0-1%, give or take a little. This is an abstraction over potential market activity that
could be generating those price changes. The environment assumes that agent actions do not have the capability to
move the price of the underlying asset.
"""


class TestSim(Environment):
    def __init__(self):
        super(TestSim, self).__init__()
        self.state = {
            "asset_price": 1.0
        }
        self.set_state_vars({
            "asset_price": "float"
        })
        self.asset_price_history = Series([1.0])
        self.asset_perc_diffs = Series()

    def tick_update(self):
        # sample Gaussian noise, add to 1.0 to function as percentage change
        self.iterate_price()

    def iterate_price(self):
        perc = 1. + np.random.normal(0, 0.02, 1)[0]
        self.state['asset_price'] = self.state['asset_price'] * perc
        self.asset_price_history.add_value(self.state['asset_price'])
        self.asset_perc_diffs.add_value(perc)
