def check_params(params):
    if "environment" not in params:
        raise Exception("Environment name must be specified.")

    if "population" not in params:
        raise Exception("Population number not specified.")

    if "agents" not in params:
        raise Exception("A list of agents must be specified.")
    else:
        for agent in params["agents"]:
            assert agent["reward_var"]
            assert agent["name"]
