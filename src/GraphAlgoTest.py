from unittest import TestCase
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo


class GraphAlgoTest(TestCase):

    def test_get_graph(self):
        g = DiGraph()
        ga = GraphAlgo()
        ga.graph = g
        ga.load_from_json('../data/A3.json')
        newG = ga.get_graph()
        self.assertEqual(g, newG)

    def test_load(self):
        g = DiGraph()
        ga = GraphAlgo()
        ga.graph = g
        self.assertTrue(ga.load_from_json('../data/A5.json'))

    def test_save(self):
        g = DiGraph()
        ga = GraphAlgo()
        ga.graph = g
        ga.load_from_json('../data/A3.json')
        self.assertTrue(ga.save_to_json('A3Test.json'))

    def test_shortest_path(self):
        graphAlgo = GraphAlgo()
        graphAlgo.graph.add_node(0)
        graphAlgo.graph.add_node(1)
        graphAlgo.graph.add_node(2)
        graphAlgo.graph.add_edge(0, 1, 1)
        graphAlgo.graph.add_edge(1, 2, 4)
        self.assertEqual(graphAlgo.shortest_path(0, 2), (5, [0, 1, 2]))

    def test_tsp(self):
        graphAlgo = GraphAlgo()
        graphAlgo.load_from_json("../data/A3.json")
        path = [7, 8, 35, 33, 32, 5]
        expected = ([8, 7, 6, 5, 6, 2, 32, 33, 34, 35], 12.82175466200503)
        self.assertEqual(expected, graphAlgo.TSP(path))

    def test_center_point(self):
        g = DiGraph()
        ga = GraphAlgo()
        ga.graph = g
        ga.load_from_json('../data/A2.json')

        str = ga.centerPoint()
        self.assertEqual("(0, 7.819910602212574)", str.__str__())
