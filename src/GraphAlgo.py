import json
import matplotlib.pyplot as plt
from src.GraphInterface import GraphInterface
from src.GraphAlgoInterface import GraphAlgoInterface
from DiGraph import DiGraph
from src.Node import Node
from typing import List


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
            pos = dic_nodes["pos"].split(',')
            self.graph.add_node(dic_nodes['id'], (float(pos[0]), float(pos[1]), float(pos[2])))
        for dic_edges in l_edges:
            self.graph.add_edge(dic_edges['src'], dic_edges['dest'], dic_edges['w'])
        return True

    def save_to_json(self, file_name: str) -> bool:
        graph_dic = {'Nodes': self.graph.get_list_nodes(), 'Edges': self.graph.get_list_edges()}
        with open(file_name, 'w') as json_file:
            json.dump(graph_dic, json_file)
        return True

    def Dijkstra(self, src: Node, dest: Node):
        mostshort = float('inf')
        queue = []
        src.setweight(0.0)
        queue.append(src)
        while len(queue) != 0:
            queue.sort()
            temp = queue.pop(0)
            if temp.getinfo() == "White":
                temp.setinfo("Black")
                if temp.getkey() == dest.getkey():
                    return temp.getweight()
                for edg in self.graph.all_out_edges_of_node(temp.getkey()):
                    temped = self.graph.edges[temp.getkey()][edg]
                    tempno = self.graph.getnode(edg)
                    if tempno.info == "White":
                        if temp.getweight() + temped.getweight() < tempno.getweight():
                            tempno.setweight(temp.getweight() + temped.getweight())
                            tempno.settag(temp.getkey())
                        queue.append(tempno)
        return mostshort

    def reset(self):
        for n in self.graph.nodes.values():
            n.setinfo("White")
            n.settag(-1)
            n.setweight(float('inf'))

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        ans = []
        ansdist = self.shortest_path_dist(id1, id2)
        if ansdist == -1:  # shode to throw exsepion
            return None
        if id1 == id2:
            return (0, [])
        self.reset()
        self.Dijkstra(self.graph.getnode(id1), self.graph.getnode(id2))
        nodesrc = self.graph.getnode(id1)
        nodedest = self.graph.getnode(id2)
        back = []
        temp = nodedest
        while temp.gettag() != -1:
            back.append(temp)
            temp = self.graph.getnode(temp.gettag())

        ans.append(nodesrc.key)

        for i in range(len(back)-1, -1, -1):
            ans.append(back[i].key)
        self.reset()
        return (ansdist, ans)

    def shortest_path_dist(self, src: int, dest: int) -> float:
        self.reset()
        ans = self.Dijkstra(self.graph.get_all_v().get(src), self.graph.get_all_v().get(dest))
        self.reset()
        if ans == 1000000:
            return -1
        return ans

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        list_ans = []
        p = []
        sec = []
        ans = 0
        for n in node_lst:
            sec.append(n)
        firstvalue = sec.pop(0)
        while len(sec) != 0:
            best = 1000000
            for nod in sec:
                temp = self.shortest_path_dist(firstvalue, nod)
                if temp < best:
                    best = temp
                    Ntemp = nod
            p = self.shortest_path(firstvalue, Ntemp)
            p =  p[1]
            for i in range(1, len( p), 1):
                list_ans.append( p[i])
            sec.remove(Ntemp)
            firstvalue = Ntemp
        for a in range(0, len(list_ans)-1, 1):
            temp = self.graph.get_edge(list_ans[a],list_ans[a+1]).getweight()
            ans = ans +temp
        return list_ans,ans

    def centerPoint(self) -> (int, float):
        c = 0
        ford = Node(-1, (0, 0, 0))
        ansdist = float('inf')
        for nod in self.graph.nodes.values():
            self.reset()
            self.Dijkstra(nod, ford)
            temp = float('-inf')
            for tempn in self.graph.nodes.values():
                if tempn.getweight() > temp:
                    temp = tempn.getweight()
            if temp < ansdist:
                ansdist = temp
                c = nod.key
        return c, ansdist

    def plot_graph(self) -> None:
        for src in self.graph.nodes.values():
            x, y, z = src.pos
            plt.plot(x, y, markersize=10, marker="o", color="green")
            plt.text(x, y, str(src.key), color="red", fontsize=14)

            for dest in self.graph.edges[src.key]:
                n_x, n_y, n_z = self.graph.nodes[dest].pos
                plt.annotate("", xy=(x, y), xytext=(n_x, n_y), arrowprops=dict(arrowstyle="<-"))
        plt.show()
