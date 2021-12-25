class Edge():
    def __init__(self, src:int,dest:int,weight:float) -> None:
        super().__init__()
        self.src = src
        self.dest = dest
        self.weight = weight
        self.info = "Wight"
        self.tag = -1

    def getsrc(self) -> int:
        return self.src

    def setsrc(self, s: int) -> None:
        self.src = s

    def getdest(self) -> int:
        return self.dest

    def setdest(self, d: int) -> None:
        self.dest = d

    def getweight(self) -> float:
        return self.weight

    def setweight(self, w: float) -> None:
        self.weight = w

    def getinfo(self) -> str:
        return self.info

    def setinfo(self, i: str) -> None:
        self.info = i

    def gettag(self) -> int:
        return self.tag

    def settag(self, t: int) -> None:
        self.tag = t



