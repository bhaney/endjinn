def search_for_agent(agent, registry):
    pass


def load_agent_files(agent):
    pass


def check_for_agent(agent, global_registry, local_registry=None):
    agent_exists = agent in [thing["name"] for thing in global_registry["agents"]]

    if local_registry and not agent_exists:
        agent_exists = agent in [thing["name"] for thing in local_registry["agents"]]

    return agent_exists


def get_registry_entry(agent, global_registry, local_registry=None):
    entry = None

    for thing in global_registry["agents"]:
        if thing["name"] == agent:
            entry = thing

    if local_registry and not entry:
        for thing in local_registry["agents"]:
            if thing["name"] == agent:
                entry = thing

    return entry
