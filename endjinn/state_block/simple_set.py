class Set(object):
    """
    Simple set class with state_var formatting helper.
    All values should be strings.
    """
    def __init__(self, vals):
        self.data = set(vals)
        self.indexed = list(self.data)

    def as_state_vars(self):
        ret = {}

        for thing in self.data:
            ret[thing] = "string"

        return ret
