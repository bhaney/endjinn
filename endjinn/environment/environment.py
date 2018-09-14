class Environment(object):
    def __init__(self):
        self.pre_cycle_hooks = []
        self.post_cycle_hooks = []
        self.cycles = 0

    def register_pre_cycle_hook(self, cb):
        if callable(cb):
            self.pre_cycle_hooks.append(cb)

    def register_post_cycle_hook(self, cb):
        if callable(cb):
            self.post_cycle_hooks.append(cb)

    def _tick(self):
        self.cycles += 1
