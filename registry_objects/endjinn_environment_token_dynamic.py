from endjinn.environment import Environment


_META = {
    "pack_name": "token_pack"
}


class TokenDynamic(Environment):
    def __init__(self, token_name,
                 per_tick_staker_rewards=None):
        super(TokenDynamic, self).__init__()
        self.state = {
            token_name + "_price": 0.1
        }
        self.set_state_vars({
            token_name + "_price": "float"
        })

    def tick_update(self):
        pass
