from endjinn.agent import Agent


_META = {}


class SimpleSpeculator(Agent):
    """
    Simple speculator agent for a single asset. Relies on observable state on env.
    Compatible with testsim environment
    """
    def __init__(self, asset_name, price_history_key, window_size=5):
        super(SimpleSpeculator, self).__init__()
        self.asset_name = asset_name
        self.window_size = window_size
        self.price_history_key = price_history_key
        # balances_fiat is a stand-in for any fiat currency
        self.set_state_vars([{
                "name": 'balances_' + asset_name,
                "type": "float"
            }, {
                "name": "balances_fiat",
                "type": "float"
            }, {
                "name": "in_position",
                "type": "int"
            }, {
                "name": "effective_fiat",
                "type": "float"
            }, {
                "name": "price_history",
                "type": "array",
                "length": window_size
            }
        ])
        self.set_actions(["buy", "sell", "pass"])
        self.state = {
            "balances_" + asset_name: 0,
            "balances_fiat": 50,
            "in_position": 0,
            "effective_fiat": 50,
            "price_history": self.get_price_history
        }
        # Key used to look up variable in environment
        self.price_key = "asset_price"
        # add callback to set 'in_position' flag on state update
        self.add_update_callback(self.set_position)
        self.add_update_callback(self.set_effective_fiat)

    def get_price_history(self):
        return getattr(self.get_env(), self.price_history_key).get_last_n(self.window_size)

    def set_position(self, agt, new_state):
        if new_state['balances_' + self.asset_name] > 0:
            self.state['in_position'] = 1
        else:
            self.state['in_position'] = 0

    def set_effective_fiat(self, agt, new_state):
        price = self.get_env().state[self.price_key]
        self.state['effective_fiat'] = self.state['balances_fiat'] + (self.state['balances_' + self.asset_name] * price)

    @property
    def buy_amount(self):
        return self.state['balances_fiat']

    @property
    def sell_amount(self):
        return self.state['balances_' + self.asset_name]
