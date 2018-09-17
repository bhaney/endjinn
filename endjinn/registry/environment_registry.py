def search_for_environment(env):
    pass


def load_environment_files(env):
    pass


def check_for_environment(env, global_registry, local_registry=None):
    env_exists = env in [thing["name"] for thing in global_registry["environments"]]

    if local_registry and not env_exists:
        env_exists = env in [thing["name"] for thing in local_registry["environments"]]

    return env_exists


def get_registry_entry(env, global_registry, local_registry=None):
    entry = None

    for thing in global_registry["environments"]:
        if thing["name"] == env:
            entry = thing

    if local_registry and not entry:
        for thing in local_registry["environments"]:
            if thing["name"] == env:
                entry = thing

    return entry
