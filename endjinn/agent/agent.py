import numpy as np


class Agent(object):
    def __init__(self, update_cbs=None):
        self.state = {}
        self.update_cbs = update_cbs
        self.actions = None
        self.state_vars = None

    def _update(self, new_state):
        self.state = new_state

        if len(self.update_cbs):
            for cb in self.update_cbs:
                if callable(cb):
                    cb(self, new_state)

    def set_actions(self, actions):
        assert isinstance(actions, list)
        self.actions = actions

    def predict_action(self, inp, policy):
        idx = np.argmax(policy.model.predict(inp))
        return self.actions[idx]

    def _set_varmap(self):
        if not self.state_vars:
            raise Exception("state_vars on agent not set.")

    def set_state_vars(self, state_vars):
        for key, val in state_vars.iteritems():
            assert val in ["float", "int", "string"]

        self.state_vars = state_vars

