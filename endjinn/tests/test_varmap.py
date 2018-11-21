from endjinn.ml.varmap import VarMap


def test_varmap():
    state_vars = [{
        "name": "float_var",
        "type": "float"
    }, {
        "name": "string_var",
        "type": "string",
        "values": ["value_one", "value_two"]
    }, {
        "name": "array_var",
        "type": "array",
        "length": 3
    }]
    vm = VarMap(state_vars)
    inp = vm.get_input({
        "float_var": 7.0,
        "string_var": "value_two",
        "array_var": [1.0, 2.0, 3.0]
    })
    assert inp[0] == 7.0
    assert inp[1] == 0
    assert inp[2] == 1
    assert inp[3] == 1.0
    assert inp[4] == 2.0
    assert inp[5] == 3.0
