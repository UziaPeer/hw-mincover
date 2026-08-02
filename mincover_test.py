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


def test_new_cases():
    # your new tests here
   
def is_vertex_cover(graph, cover):
    return all(u in cover or v in cover for u, v in graph.edges())


def brute_force_mincover_size(graph):
    vertices = list(graph.nodes())

    for r in range(len(vertices) + 1):
        for subset in itertools.combinations(vertices, r):
            if is_vertex_cover(graph, set(subset)):
                return r

    return len(vertices)


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


def test_random_small_graphs():
    for n in range(2, 9):
        for seed in range(5):
            graph = nx.gnp_random_graph(n, 0.35, seed=seed)
            cover = mincover(graph)

            assert is_vertex_cover(graph, cover)
            assert len(cover) == brute_force_mincover_size(graph)


def test_large_random_graphs():
    for seed in range(3):
        graph = nx.gnm_random_graph(50, 1000, seed=seed)
        cover = mincover(graph)

        assert is_vertex_cover(graph, cover)
        assert len(cover) <= 50
    pass
