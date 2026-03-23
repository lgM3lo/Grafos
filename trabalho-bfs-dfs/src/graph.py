# trabalho-bfs-dfs/src/graph.py

class Bag:
    def __init__(self):
        self._items = []

    def add(self, item):
        self._items.append(item)

    def __iter__(self):
        return iter(self._items)

    def __len__(self):
        return len(self._items)


class Graph:

    def __init__(self, v):
        self.V = v
        self.E = 0
        self.adj = {}

        for v in range(self.V):
            self.adj[v] = Bag()

    def add_edge(self, v, w):
        v, w = int(v), int(w)
        self.adj[v].add(w)
        self.adj[w].add(v)
        self.E += 1

    def degree(self, v):
        return len(self.adj[v])