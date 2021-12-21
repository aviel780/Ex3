class Edge:
    def __init__(self,s:int,d:int,w:float):
        self.src = s
        self.dest = d
        self.weight = w

    def get_src(self):
        return self.src
    def get_dest(self):
        return self.dest
    def get_weight(self):
        return self.weight


