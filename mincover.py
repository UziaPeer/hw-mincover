# import subprocess, sys
# subprocess.check_call([sys.executable, "-m", "pip", "install", "cvxpy"], stdout=subprocess.DEVNULL)
# subprocess.check_call([sys.executable, "-m", "pip", "install", "networkx>=3.4"], stdout=subprocess.DEVNULL)

import numpy as np
np.float_ = np.float64

import networkx as nx
import cvxpy


def mincover(graph: nx.Graph) -> set:
    """
    Return a minimum-cardinality vertex cover in the given graph.
    
    >>> len(mincover(nx.Graph([(1,2),(2,3)])))
    1
    >>> len(mincover(nx.Graph([(1,2),(2,3),(3,1)])))
    2
    >>> len(mincover(nx.Graph([(1,2),(2,3),(3,4),(4,1)])))
    2
    >>> len(mincover(nx.Graph([])))
    0
    """
    if graph.number_of_edges() == 0:
        return set()

    vertices = list(graph.nodes())
    place = {v: i for i, v in enumerate(vertices)}

    x = cvxpy.Variable(len(vertices), boolean=True)
    constraints = [x[place[u]] + x[place[v]] >= 1 for u, v in graph.edges()]

    problem = cvxpy.Problem(cvxpy.Minimize(cvxpy.sum(x)), constraints)
    problem.solve(solver=cvxpy.SCIPY)

    return {vertices[i] for i in range(len(vertices)) if x.value[i] > 0.5}


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())

    # Use this code for testing via console input-output:
    # edges=eval(input())
    # graph = nx.Graph(edges)
    # print(len(mincover(graph)))
