from endjinn.action.update_dict import UpdateDict


def handler(agent_state, global_state, params):
    """
    :param agent_state: State dict of the agent taking the action
    :param global_state:
    :param params: Parameters of the action itself
    :return: UpdateDict
    """
    ud = UpdateDict({})
    # pass is a noop, so simply return empty update dict
    return ud
