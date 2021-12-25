from _ast import List
import json
from src.GraphInterface import GraphInterface
from src.GraphAlgoInterface import GraphAlgoInterface
from DiGraph import DiGraph


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, g: DiGraph = DiGraph()) -> None:
        # super().__init__()
        self.graph = g

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        with open(file_name, 'r') as f:
            data = json.load(f)
        l_nodes = data["Nodes"]
        l_edges = data["Edges"]
        for dic_nodes in l_nodes:
            self.graph.add_node(dic_nodes['id'], dic_nodes['pos'])
        for dic_edges in l_edges:
            self.graph.add_edge(dic_edges['src'], dic_edges['dest'], dic_edges['w'])
        return True

    def save_to_json(self, file_name: str) -> bool:
        graph_dic = {'Nodes': self.graph.get_list_nodes(), 'Edges': self.graph.get_list_edges()}
        with open(file_name, 'w') as json_file:
            json.dump(graph_dic, json_file)
        return True

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        return None

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        return None

    def centerPoint(self) -> (int, float):
        return None

    def plot_graph(self) -> None:
        return None
