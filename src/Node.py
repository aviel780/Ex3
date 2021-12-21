class Node:
    def __init__(self, i: int, p: tuple):
        self.id = i
        self.pos = p
        self.tag = 0
        self.weight = 0

    def __init__(self, i: int, p: tuple, w:float):
        self.id = i
        self.pos = p
        self.tag = 0
        self.weight = w

    def get_id(self):
        return self.id

    def get_pos(self):
        return self.pos

    def get_tag(self):
        return self.tag

    def get_weight(self):
        return self.weight

    def set_tag(self, tag):
        self.tag = tag

    def set_weight(self, weight):
        self.weight = weight


