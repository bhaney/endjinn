"""
TokenDynamic is the main class for handling normal tokens as well as stablecoins.
"""
from endjinn.environment import Environment


_META = {
    "pack_name": "token_pack"
}


class TokenDynamic(Environment):
    def __init__(self, token_name,
                 token_type="standard",
                 per_tick_staker_rewards=None):
        super(TokenDynamic, self).__init__()

        if token_type not in ["standard", "stable"]:
            raise Exception("token_type must be one of 'erc', 'stable'")

        self.token_type = "erc"
        self.state = {
            token_name + "_price": 0.1
        }
        self.set_state_vars({
            token_name + "_price": "float"
        })

    def tick_update(self):
        pass

    def price_update(self):
        # Defines a price update function based on buys and sells in last tick
        pass
