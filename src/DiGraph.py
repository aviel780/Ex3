import json
import string
from src.Edge import Edge
from src.Node import Node
from src.GraphInterface import GraphInterface


class DiGraph(GraphInterface):
       nodes = {}
       edges = {}
       mc = 0
       def __init__(self) -> None:
              super().__init__()
              self.nodes = {}
              self.edges = {}
              self.mc = 0

       def v_size(self) -> int:
              return len(self.nodes)

       def e_size(self) -> int:
              return len(self.nodes)

       def get_all_v(self) -> dict:
              return self.nodes

       def all_in_edges_of_node(self, id1: int) -> dict:
              return self.nodes[id1]

       def all_out_edges_of_node(self, id1: int) -> dict:
              raise NotImplementedError

       def get_mc(self) -> int:
              return self.mc

       def add_edge(self, id1: int, id2: int, weight: float) -> bool:
              temp = Edge(id1, id2, weight)
              if id1 not in self.edges.keys():
                     return False
              if id1 in self.edges.keys() and id2 in self.edges[id1]:# find if id2 is alredy dest in id1
                     return False
              self.edges[id1] = temp
              self.mc = self.mc + 1
              return True

       def add_node(self, node_id: int, pos: tuple = None) -> bool:
              temp = Node(node_id,pos)
              if temp.id in self.nodes.keys():
                     return False
              self.nodes[node_id]= temp
              self.edges[node_id] = {}
              self.mc =self.mc+1
              return True

       def remove_node(self, node_id: int) -> bool:# need to dalet the edges
              if node_id not in self.nodes.keys():
                     return False
              self.nodes[node_id] = None

              for i in self.edges.keys():



       def remove_edge(self, node_id1: int, node_id2: int) -> bool:
              raise NotImplementedError

