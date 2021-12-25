from _ast import List
import json
from src.GraphInterface import GraphInterface
from src.GraphAlgoInterface import GraphAlgoInterface
from DiGraph import DiGraph
from src.Node import Node


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, g: DiGraph = DiGraph()) -> None:
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

    def Dijkstra(self, src: Node, dest: Node):
        shortest = 1000000
        queue = []
        src.setweight(0.0)
        queue.append(src)
        while len(queue) != 0:
            temp = queue.pop(0)
            if temp.getinfo() == "White":
                temp.setinfo("Black")
                if temp.getkey() == dest.getkey():
                    return temp.getweight()
                for e in self.graph.all_out_edges_of_node(temp.getkey()):
                    ed = e
                    no = self.graph.getnode(ed.getdest)
                    if ed.info == "White":
                        if temp.getweight() + ed.getweight() < no.getweight():
                            no.setweight(temp.getweight() + ed.getweight())
                            no.settag(temp.getkey())
                        queue.append(no)
        return shortest

    def reset(self):
        for n in self.graph.nodes.items():
            n.setinfo("White")
            n.settag(-1)
            n.setweight(1000000)

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        ans =[]
        ansdist = self.Dijkstra(self.graph.getnode(id1),self.graph.getnode(id2))

        if ansdist == -1:# shode to throw exsepion
            return None
        if id1 == id2:
            return (0,[])
        self.reset()
        self.Dijkstra(self.graph.getnode(id1),self.graph.getnode(id2))
        Nsrc = self.graph.getnode(id1)
        Ndest = self.graph.getnode(id2)
        revers = []
        temp = Ndest
        while temp.settag() == -1:
            revers.append(temp)
            temp = self.graph.getnode(temp.gettag())
        ans.append(Nsrc)

        for i in range(len(revers),0,-1):
            ans.append(revers[i]) ###################################################### maybe aproblem

        self.reset()
        return (ansdist,ans)

    def shortest_path_dist(self,src:int,dest:int)->float:
        self.reset()
        ans = self.Dijkstra(self.graph.getnode(src),self.graph.getnode(dest))
        self.reset()
        if ans  == 1000000:
            return -1
        return ans

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        return None

    def centerPoint(self) -> (int, float):
        return None

    def plot_graph(self) -> None:
        return None
