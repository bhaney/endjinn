import numpy as np
import networkx as nx


class Graph(object):
    """
    Class for representing state graph with valid transitions.
    """
    def __init__(self, node_labels=None, edgelist=None, stateful=False, weighted=False):
        self.stateful = stateful
        self.weighted = weighted
        self.graph = None
        self.current_state = None
        self.n_nodes = None

        if edgelist and node_labels:
            self.from_edgelist(edgelist, node_labels)

    def from_edgelist(self, edgelist, node_labels=None):
        """

        :param edgelist: (source, dest) numbers.
        :param node_labels: List of strings. Labeles for each node.
        :return:
        """
        if node_labels:
            if np.max(edgelist) != len(node_labels) - 1:
                raise Exception("Node labels must be of same size as number of nodes.")

        self.graph = nx.DiGraph()

        for i in range(len(node_labels)):
            self.graph.add_node(i, attr_dict={"label": node_labels[i]})

        self.n_nodes = len(node_labels)

        for thing in edgelist:
            self.graph.add_edge(thing[0], thing[1])

    def is_valid_edge(self, source, dest):
        return self.graph.has_edge(source, dest)

    def set_initial_state(self, state):
        self.current_state = state

    def transition(self, dest):
        if not self.stateful:
            raise Exception("stateful flag is false on this class instance. Set stateful=True during instantiaion to "
                            "enable state transitions.")
        else:
            if not self.current_state:
                raise Exception("Call set_initial_state before attempting transition to another state.")

            if self.is_valid_edge(self.current_state, dest):
                self.current_state = dest

    def get_current_state_as_one_hot(self):
        vec = np.zeros(self.n_nodes)
        vec[self.current_state] = 1

        return vec


