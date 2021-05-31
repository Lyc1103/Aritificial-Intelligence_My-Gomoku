from numpy import *


class Vertex:
    def __init__(self, node):
        self.id = node
        self.BorW = 0
        self.link_N_S = 0
        self.link_EN_WS = 0
        self.link_E_W = 0
        self.link_ES_WN = 0
        self.N = None
        self.EN = None
        self.E = None
        self.ES = None
        self.S = None
        self.WS = None
        self.W = None
        self.WN = None
        # [][0]: numerator, [][1]: denominator
        self.black_rate = zeros((19 * 19, 2))
        self.white_rate = zeros((19 * 19, 2))

    def add_neighbor(self, neighbor, dir):
        if dir == "N":
            self.N = neighbor
        elif dir == "EN":
            self.EN = neighbor
        elif dir == "E":
            self.E = neighbor
        elif dir == "ES":
            self.ES = neighbor
        elif dir == "S":
            self.S = neighbor
        elif dir == "WS":
            self.WS = neighbor
        elif dir == "W":
            self.W = neighbor
        elif dir == "WN":
            self.WN = neighbor

    def reset(self):
        self.BorW = 0
        self.link_N_S = 0
        self.link_EN_WS = 0
        self.link_E_W = 0
        self.link_ES_WN = 0


# end class Vertex


class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0
        self.black_path = []
        self.white_path = []

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, dir):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], dir)

    def get_vertices(self):
        return self.vert_dict.keys()

    def add_to_black_path(self, id):
        self.black_path.append(id)

    def add_to_white_path(self, id):
        self.white_path.append(id)

    def clear_path(self):
        id = self.black_path.pop()
        while id != None:
            id = self.black_path.pop()
        id = self.white_path.pop()
        while id != None:
            id = self.white_path.pop()


# end class Graph


def FlagInGraph(gomoku, x, y, borw):
    xy_id = str(x) + "_" + str(y)
    v = gomoku.graph.get_vertex(xy_id)
    v.BorW = borw
    # print(v.BorW)

    # check if it has any neighbor
    # calculate the hightest point it gets
    if v.N.BorW == borw:
        if v.S.BorW == borw:
            v.link_N_S = v.N.link_N_S + v.S.link_N_S + 1
            tmp = v.S
            while tmp.BorW == borw:
                tmp.link_N_S = v.link_N_S
                tmp = tmp.S
        else:
            v.link_N_S = v.N.link_N_S + 1
        tmp = v.N
        while tmp.BorW == borw:
            tmp.link_N_S = v.link_N_S
            tmp = tmp.N
    elif v.S.BorW == borw:
        v.link_N_S = v.S.link_N_S + 1
        tmp = v.S
        while tmp.BorW == borw:
            tmp.link_N_S = v.link_N_S
            tmp = tmp.S
    else:
        v.link_N_S = 1

    if v.EN.BorW == borw:
        if v.WS.BorW == borw:
            v.link_EN_WS = v.EN.link_EN_WS + v.WS.link_EN_WS + 1
            tmp = v.WS
            while tmp.BorW == borw:
                tmp.link_EN_WS = v.link_EN_WS
                tmp = tmp.WS
        else:
            v.link_EN_WS = v.EN.link_EN_WS + 1
        tmp = v.EN
        while tmp.BorW == borw:
            tmp.link_EN_WS = v.link_EN_WS
            tmp = tmp.EN
    elif v.WS.BorW == borw:
        v.link_EN_WS = v.WS.link_EN_WS + 1
        tmp = v.WS
        while tmp.BorW == borw:
            tmp.link_EN_WS = v.link_EN_WS
            tmp = tmp.WS
    else:
        v.link_EN_WS = 1

    if v.E.BorW == borw:
        if v.W.BorW == borw:
            v.link_E_W = v.E.link_E_W + v.W.link_E_W + 1
            tmp = v.W
            while tmp.BorW == borw:
                tmp.link_E_W = v.link_E_W
                tmp = tmp.W
        else:
            v.link_E_W = v.E.link_E_W + 1
        tmp = v.E
        while tmp.BorW == borw:
            tmp.link_E_W = v.link_E_W
            tmp = tmp.E
    elif v.W.BorW == borw:
        v.link_E_W = v.W.link_E_W + 1
        tmp = v.W
        while tmp.BorW == borw:
            tmp.link_E_W = v.link_E_W
            tmp = tmp.W
    else:
        v.link_E_W = 1

    if v.ES.BorW == borw:
        if v.WN.BorW == borw:
            v.link_ES_WN = v.ES.link_ES_WN + v.WN.link_ES_WN + 1
            tmp = v.WN
            while tmp.BorW == borw:
                tmp.link_ES_WN = v.link_ES_WN
                tmp = tmp.WN
        else:
            v.link_ES_WN = v.ES.link_ES_WN + 1
        tmp = v.ES
        while tmp.BorW == borw:
            tmp.link_ES_WN = v.link_ES_WN
            tmp = tmp.ES
    elif v.WN.BorW == borw:
        v.link_ES_WN = v.WN.link_ES_WN + 1
        tmp = v.WN
        while tmp.BorW == borw:
            tmp.link_ES_WN = v.link_ES_WN
            tmp = tmp.WN
    else:
        v.link_ES_WN = 1

    if v.link_N_S >= 5 or v.link_EN_WS >= 5 or v.link_E_W >= 5 or v.link_ES_WN >= 5:
        if borw == 2:
            # print("You Win!")
            return 1
        else:
            # print("You Loss...")
            return -1
    return 0


# end func FlagInGraph
