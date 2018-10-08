import numpy as np
from endjinn.ml.varmap import VarMap


class Agent(object):
    def __init__(self, update_cbs=None):
        self.state = {}
        self.update_cbs = update_cbs
        self.actions = None
        self.state_vars = None
        self.varmap = None
        # action_params should be a list of attributes which get passed to each action as arguments
        self.action_params = None

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
            raise Exception("state_vars on agent not set. Call set_state_vars first.")

        self.varmap = VarMap(self.state_vars)

    def set_state_vars(self, state_vars):
        for var in state_vars:
            assert var["type"] in ["float", "int", "string"]

        self.state_vars = state_vars
        self._set_varmap()

    def get_input(self):
        return self.varmap.get_input(self.state)

    def get_action_params(self):
        if not self.action_params:
            raise Exception("action_params not present on Agent. Be sure to implement in subclass.")

        temp = {}

        for key in self.action_params:
            temp[key] = getattr(self, key)

        return temp
