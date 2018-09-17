def search_for_action(action):
    pass


def load_action_files(action):
    pass


def get_registry_entry(action, global_registry, local_registry=None):
    entry = None

    for thing in global_registry["actions"]:
        if thing["name"] == action:
            entry = thing

    if local_registry and not entry:
        for thing in local_registry["actions"]:
            if thing["name"] == action:
                entry = thing

    return entry
