# import subprocess, sys
# subprocess.check_call([sys.executable, "-m", "pip", "install", "cvxpy"], stdout=subprocess.DEVNULL)
# subprocess.check_call([sys.executable, "-m", "pip", "install", "networkx>=3.4"], stdout=subprocess.DEVNULL)

import networkx as nx, cvxpy, numpy as np
np.float_ = np.float64

def mincover(graph: nx.Graph)->set:
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
    # Your code here.
     edges = list(graph.edges())

    if len(edges) == 0:
        return set()

    vertices = list(graph.nodes())
    index = {v: i for i, v in enumerate(vertices)}

    x = cvxpy.Variable(len(vertices), boolean=True)

    constraints = []
    for u, v in edges:
        constraints.append(x[index[u]] + x[index[v]] >= 1)

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

