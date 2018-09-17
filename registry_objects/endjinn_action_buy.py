from endjinn.action.update_dict import UpdateDict


def handler(agent_state, global_state, params):
    """
    :param agent_state: State dict of the agent taking the action
    :param global_state:
    :param params: Parameters of the action itself
    :return: UpdateDict
    """
    price = global_state[params["price_key"]]
    less_amt = params["buy_amount"] * price
    total = params["buy_amount"] / price
    update_params = {"balances_usd": less_amt, "balances_" + params["price_key"]: total}

    ud = UpdateDict(update_params)

    return ud
