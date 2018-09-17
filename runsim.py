import argparse
import json
import endjinn
import endjinn.registry.agent_registry
import endjinn.registry.environment_registry
import endjinn.registry.action_registry


parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--file', default="endjinnfile.json")
args = parser.parse_args()


if __name__ == "__main__":
    with open(args.file) as f:
        sim_params = json.load(f)

    # Check params are correctly structured
    endjinn.check_params(sim_params)
    env_name = sim_params.get("environment")

    if not env_name:
        raise Exception("Environment name must be specified in endjinn file.")

    population = sim_params.get("population")

    env_exists = endjinn.registry.environment_registry.search_for_environment(env_name)

    if not env_exists:
        raise Exception("Environment not found in registry. Check the environment name.")

    # Check that each agent has an entry
    for agent in sim_params["agents"]:
        if not endjinn.registry.agent_registry.search_for_agent(agent["name"]):
            raise Exception("Agent %s not found in registry. Check the agent name.")


