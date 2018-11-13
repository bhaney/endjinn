from endjinn.environment import Environment


class TestSim(Environment):
    def __init__(self):
        super(TestSim, self).__init__()
        self.state = {
            "coin_price": 1.0
        }
        self.set_state_vars({
            "coin_price": "float"
        })

    def tick_update(self):
        pass
