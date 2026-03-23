# trabalho-bfs-dfs/src/breadth_first_paths.py

class Queue:
    def __init__(self):
        self._items = []

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        return self._items.pop(0)

    def is_empty(self):
        return len(self._items) == 0


class BreadthFirstPaths:

    def __init__(self, G, s):
        self.marked = [False] * G.V
        self.edge_to = [None] * G.V
        self.s = s
        self._bfs(G, s)

    def _bfs(self, G, s):
        q = Queue()
        self.marked[s] = True
        q.enqueue(s)

        while not q.is_empty():
            v = q.dequeue()
            for w in G.adj[v]:
                if not self.marked[w]:
                    self.edge_to[w] = v
                    self.marked[w] = True
                    q.enqueue(w)

    def has_path_to(self, v):
        return self.marked[v]

    def path_to(self, v):
        if not self.has_path_to(v):
            return None

        path = []
        x = v
        while x != self.s:
            path.append(x)
            x = self.edge_to[x]
        path.append(self.s)

        return list(reversed(path))