from endjinn.agent import Agent


_META = {
    "pack_name": "token_pack"
}


class Staker(Agent):
    def __init__(self, token_name):
        super(Staker, self).__init__()
        self.token_name = token_name
        self.set_state_vars([{
                "name": 'balances_' + token_name,
                "type": "float"
            }, {
                "name": "balances_eth",
                "type": "float"
            }
        ])
        self.set_actions(["stake", "unstake"])
        self.state = {
            "balances_" + token_name: 0,
            "balances_eth": 50
        }
        # Key used to look up variable in environment
        self.price_key = token_name + "_price"

    @property
    def buy_amount(self):
        return self.state['balances_eth']

    @property
    def sell_amount(self):
        return self.state['balances_' + self.token_name]
