from src.Edge import Edge
from src.GraphInterface import GraphInterface
from src.Node import Node


class DiGraph(GraphInterface):
    # init the graph
    def __init__(self) -> None:
        super().__init__()
        self.nodes = {}
        self.edges = {}
        self.SizeOfEdge = 0
        self.list_nodes = []
        self.list_edges = []
        self.mc = 0

    # return the size of the nodes
    def v_size(self) -> int:
        return len(self.nodes)

    # return the size of the edges
    def e_size(self) -> int:
        return self.SizeOfEdge

    # return all the nodes in dicsenery
    def get_all_v(self) -> dict:
        return self.nodes

    # return all the nodes in list
    def get_list_nodes(self) -> list:
        return self.list_nodes

    # return all the edges in list
    def get_list_edges(self) -> list:
        return self.list_edges

    # return all the nodes thet point to this node
    def all_in_edges_of_node(self, id1: int) -> dict:
        ans = {}
        #going over all the nodes (the key value in edge reprsent the src node)
        for s in self.edges.keys():
            #going over all the dest nodes
            for d in self.edges[s].keys():
                if d == id1:
                    if s not in ans.keys():
                        ans[s] = self.edges[s][id1]

        return ans

    # return all the nodes thet the node point at
    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.edges[id1]

    # return the number of the acsions how did on the graph
    def get_mc(self) -> int:
        return self.mc

    # add edge to the graph
    # id1 - src , id2 - dst
    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        #if dont have the src or the dest in the nodes graph
        if id1 not in self.nodes.keys() or id2 not in self.nodes.keys():
            return False
        edge = Edge(id1, id2, weight)
        if id1 in self.edges.keys():
            #if the edge allredy vesist in the graph
            if id2 in self.edges[id1].keys():
                return False
            else:
                self.edges[id1][id2] = edge
                self.SizeOfEdge += 1
        else:
            edge = Edge(id1, id2, weight)
            #we create at as dict in dict the key of the first dict is the src node the value is the sconde dict,
            #in the second dict the key is the dest node and the value is all the permetrs of the edge
            self.edges[id1] = {id2: edge}
            self.SizeOfEdge += 1
        # save into a list all the permetrs we need to the save file
        self.list_edges.append({'src': id1, 'dest': id2, 'w': weight})
        self.mc = self.mc + 1
        return True

    # add node to the graph
    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        # if the node all redy exsist
        if node_id in self.nodes.keys():
            return False
        else:
            self.nodes[node_id] = Node(node_id, pos)

        self.list_nodes.append({'id': node_id, 'pos': pos})
        self.mc = self.mc + 1
        return True

    # return node by his id
    def getnode(self, id: int) -> Node:
        return self.nodes[id]

    # remove node frome the graph
    def remove_node(self, node_id: int) -> bool:
        if node_id not in self.nodes.keys():
            return False
        else:
            # remove from nodes
            self.nodes.pop(node_id)
        # remove all the edges that the node is the src
        if node_id in self.edges.keys():
            self.edges.pop(node_id)
        for i in self.list_edges:
            if i['src'] == node_id or i['dest'] == node_id:
                self.list_edges.remove(i)
                self.SizeOfEdge -= 1

        self.mc = self.mc + 1
        return True

    # remove edge from the graph
    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id1 not in self.edges.keys():
            return False
        if node_id1 in self.edges.keys() and node_id2 not in self.edges[node_id1].keys():
            return False
        else:
            self.edges[node_id1].pop(node_id2)
            for i in self.list_edges:
                if i['src'] == node_id1 and i['dest'] == node_id2:
                    self.list_edges.remove(i)
                    break
            # self.list_edges[node_id1].pop(node_id2)
            self.SizeOfEdge -= 1
        self.mc = self.mc + 1
        return True

    # return edge by src and dest
    def get_edge(self, src: int, dest: int):
        return self.edges[src][dest]
