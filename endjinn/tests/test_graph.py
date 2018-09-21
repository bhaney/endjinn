from endjinn.state_block import Graph


def test_graph():
    g = Graph(stateful=True)
    g.from_edgelist([[0, 1], [1, 2], [2, 0]], ["zero", "one", "two"])

    assert g.n_nodes == 3
    assert not g.current_state

    g.set_initial_state(2)

    assert g.current_state == 2

    g.transition(0)

    assert g.current_state == 0
