class Edge():
    def __init__(self, src:int,dest:int,weight:float) -> None:
        super().__init__()
        self.src = src
        self.dest = dest
        self.weight = weight
        self.info = "Wight"
        self.tag = -1
