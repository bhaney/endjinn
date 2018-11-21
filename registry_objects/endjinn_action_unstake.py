from endjinn.action.update_dict import UpdateDict

_META = {
    "pack_name": "token_pack"
}


def handler(agent_state, global_state, params):
    """
    :param agent_state: State dict of the agent taking the action
    :param global_state:
    :param params: Parameters of the action itself
    :return: UpdateDict
    """
    price = global_state[params["price_key"]]
    less_amt = params["sell_amount"] / price
    total = params["sell_amount"] * price
    update_params = {"balances_eth": total, "balances_" + params["price_key"]: less_amt}

    ud = UpdateDict(update_params)

    return ud
