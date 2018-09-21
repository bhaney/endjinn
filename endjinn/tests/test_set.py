from endjinn.state_block import Set


def test_set():
    s = Set(["aggressive", "neutral", "conservative"])
    assert s.indexed == ["aggressive", "neutral", "conservative"]

    state_vars = s.as_state_vars()

    assert state_vars["aggressive"] == "string"
    assert state_vars["conservative"] == "string"
    assert state_vars["neutral"] == "string"
