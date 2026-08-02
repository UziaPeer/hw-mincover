import pytest
import networkx as nx
from mincover import mincover
from testcases import parse_testcases

testcases = parse_testcases("testcases.txt")

def run_testcase(input:str):
    graph = nx.Graph(input)
    cover = mincover(graph)
    return len(cover)

@pytest.mark.parametrize("testcase", testcases, ids=[testcase["name"] for testcase in testcases])
def test_cases(testcase):
    actual_output = run_testcase(testcase["input"])
    assert actual_output == testcase["output"], f"Expected {testcase['output']}, got {actual_output}"


def is_vertex_cover(graph, cover):
    return all(u in cover or v in cover for u, v in graph.edges())


def test_new_cases():
    graph = nx.Graph()
    assert mincover(graph) == set()

    graph = nx.path_graph(5)
    cover = mincover(graph)
    assert is_vertex_cover(graph, cover)
    assert len(cover) == 2

    graph = nx.cycle_graph(6)
    cover = mincover(graph)
    assert is_vertex_cover(graph, cover)
    assert len(cover) == 3

    graph = nx.complete_graph(8)
    cover = mincover(graph)
    assert is_vertex_cover(graph, cover)
    assert len(cover) == 7

    graph = nx.star_graph(10)
    cover = mincover(graph)
    assert is_vertex_cover(graph, cover)
    assert len(cover) == 1


def test_large_random_graph():
    graph = nx.gnm_random_graph(50, 1000, seed=1)
    cover = mincover(graph)

    assert is_vertex_cover(graph, cover)
    assert len(cover) <= 50
    pass
