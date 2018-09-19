class UpdateDict(object):
    def __init__(self, params):
        self.params = params

    def apply(self, state_dict):
        """
        Applies the updates to a state dict as from an agent. Helper merge method.

        :param state_dict:
            State of an agent from before an action was taken
        :return:
        """
        for key, val in self.params.iteritems():
            if key in state_dict:
                if isinstance(self.params[key], int) or isinstance(self.params[key], float):
                    state_dict[key] += self.params[key]
                elif isinstance(self.params[key], str):
                    state_dict[key] = self.params[key]
