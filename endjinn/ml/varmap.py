import numpy as np


class VarMap(object):
    def __init__(self, state_vars):
        self.var_types = {}
        for var in state_vars:
            assert "name" in var
            assert "type" in var
            self.var_types[var["name"]] = var["type"]

        self.index_slices = {}
        self.val_pos = {}
        self.input_length = None

        idx = 0

        for var in state_vars:
            if var["type"] == "int" or var["type"] == "float":
                self.index_slices[var["name"]] = (idx,)
                self.val_pos[var["name"]] = idx
                idx += 1
            elif var["type"] == "string":
                self.index_slices[var["name"]] = (idx, idx + len(var["values"]))

                for j, val in enumerate(var["values"]):
                    self.val_pos[val] = idx + j

                idx += len(var["values"])
            elif var["type"] == "array":
                self.index_slices[var["name"]] = (idx, idx + var["length"])

                for j in range(var["length"]):
                    val = var["name"] + ":" + str(j)
                    self.val_pos[val] = idx + j

                idx += var["length"]

        self.input_length = idx

    def get_input(self, state):
        inp = [0] * self.input_length

        for key, val in state.iteritems():
            if callable(val):
                _val = val()
                val = _val

            slc = self.index_slices[key]

            if len(slc) == 1:
                inp[self.val_pos[key]] = val
            elif len(slc) == 2 and self.var_types[key] == "string":
                inp[self.val_pos[val]] = 1
            elif len(slc) == 2 and self.var_types[key] == "array":
                for j in range(len(val)):
                    inp[self.val_pos[key + ":" + str(j)]] = val[j]

        return np.array(inp)
