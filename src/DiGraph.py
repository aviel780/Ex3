from src.GraphInterface import GraphInterface


class DiGraph(GraphInterface):
    def __init__(self) -> None:
        super().__init__()
        self.nodes = {}
        self.edges = {}
        self.SizeOfEdge = 0
        self.list_nodes = []
        self.list_edges = []

        self.mc = 0

    def v_size(self) -> int:
        return len(self.nodes)

    def e_size(self) -> int:
        return self.SizeOfEdge

    def get_all_v(self) -> dict:
        return self.nodes

    def get_list_nodes(self) -> list:
        return self.list_nodes

    def get_list_edges(self) -> list:
        return self.list_edges

    def all_in_edges_of_node(self, id1: int) -> dict:
        ans = {}
        for s in self.edges.keys():
            for d in self.edges[s].keys():
                if d == id1:
                    if s not in ans.keys():
                        ans[s] = self.edges[s][id1]

        return ans

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.edges[id1]

    def get_mc(self) -> int:
        return self.mc

    # id1 - src , id2 - dst
    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 not in self.nodes.keys() or id2 not in self.nodes.keys():
            return False

        if id1 in self.edges.keys():
            if id2 in self.edges[id1].keys():
                return False
            else:
                self.edges[id1][id2] = weight
                self.SizeOfEdge += 1
        else:
            self.edges[id1] = {id2: weight}
            self.SizeOfEdge += 1

        self.list_edges.append({'src' :id1 , 'dest' : id2 , 'w': weight})
        self.mc = self.mc + 1
        return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id in self.nodes.keys():
            return False
        else:
            self.nodes[node_id] = pos

        self.list_nodes.append({'id': node_id, 'pos': pos})
        self.mc = self.mc + 1
        return True

    def remove_node(self, node_id: int) -> bool:
        if node_id not in self.nodes.keys():
            return False
        else:
            # remove from nodes
            self.nodes.pop(node_id)

        # remove all the edges that the node is the src
        if node_id in self.edges.keys():
            self.edges.pop(node_id)
        # remove all the edges that the node is the dst
        for id1 in self.edges.keys():
            for id2 in self.edges[id1].keys():
                if id2 == node_id:
                    self.edges[id1].pop(node_id)
                    self.SizeOfEdge -= 1

        self.mc = self.mc + 1
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id1 not in self.edges.keys():
            return False
        if node_id1 in self.edges.keys() and node_id2 not in self.edges[node_id1].keys():
            return False
        else:
            self.edges[node_id1].pop(node_id2)
            self.SizeOfEdge -= 1
        self.mc = self.mc + 1
        return True
