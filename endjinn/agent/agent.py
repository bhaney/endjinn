class Agent(object):
    def __init__(self, update_cbs=[]):
        self.state = {}
        self.update_cbs = update_cbs

    def _update(self, new_state):
        self.state = new_state

        if len(self.update_cbs):
            for cb in self.update_cbs:
                if callable(cb):
                    cb(self, new_state)

    def predict_action(self, percept):
        raise NotImplementedError()
