class Node():
    def _init_(self, node_id:int,pos:tuple) -> None:
       # super()._init_()
        self.key = node_id
        self.weight = 1000000
        self.info = "Wight"
        self.tag = -1
        self.pos = pos

    def getkey(self) -> int:
        return self.key

    def setkey(self, k:int) -> None:
        self.key = k

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

    def getpos(self) -> tuple:
        return self.pos

    def setpos(self, p: tuple) -> None:
        self.pos = p

    def _repr_(self):
        return f"({self.key} , {self.pos})"

    def _lt_(self, other):
        return self.weight<other.weight

    def _le_(self, other):
        return self.weight <= other.weight

    def _eq_(self, other):
        return self.weight == other.weight

    def _ne_(self, other):
        return self.weight != other.weight

    def _gt_(self, other):
        return self.weight>other.weight

    def _ge_(self, other):
        return self.weight<=other.weight