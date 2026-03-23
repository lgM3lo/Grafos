import sys
import os

# Ajuste de caminho (para rodar fora do Colab também)
sys.path.append(os.path.dirname(__file__))

from graph import Graph
from depth_first_paths import DepthFirstPaths
from breadth_first_paths import BreadthFirstPaths


# ===== FUNÇÕES AUXILIARES (fora do algs4) =====

def dfs_order(G, s):
    marked = [False] * G.V
    order = []

    def dfs(v):
        marked[v] = True
        order.append(v)
        for w in G.adj[v]:
            if not marked[w]:
                dfs(w)

    dfs(s)
    return order


def bfs_order(G, s):
    from breadth_first_paths import Queue

    marked = [False] * G.V
    order = []

    q = Queue()
    marked[s] = True
    q.enqueue(s)

    while not q.is_empty():
        v = q.dequeue()
        order.append(v)
        for w in G.adj[v]:
            if not marked[w]:
                marked[w] = True
                q.enqueue(w)

    return order


# ===== MAIN =====

def main():
    estados = ["AL", "BA", "CE", "MA", "PB", "PE", "PI", "RN", "SE"]
    estado_to_id = {est: i for i, est in enumerate(estados)}

    origem = input("Estado origem: ").upper()
    destino = input("Estado destino: ").upper()

    if origem not in estado_to_id or destino not in estado_to_id:
        print("Estado inválido!")
        return

    s = estado_to_id[origem]
    t = estado_to_id[destino]

    # Caminho relativo ao projeto
    caminho_arquivo = os.path.join(os.path.dirname(__file__), "../dados/nordeste.txt")

    with open(caminho_arquivo) as f:
        V = int(f.readline())
        E = int(f.readline())

        g = Graph(V)

        for line in f:
            if line.strip():
                v, w = line.split()
                g.add_edge(v, w)

    dfs = DepthFirstPaths(g, s)
    bfs = BreadthFirstPaths(g, s)

    print("\n--- RESULTADOS ---")

    # 1
    print("1. Alcançável:",
          "Sim" if dfs.has_path_to(t) else "Não")

    # 2
    caminho_dfs = dfs.path_to(t)
    print("2. Caminho DFS:",
          " -> ".join(estados[v] for v in caminho_dfs) if caminho_dfs else "Não existe")

    # 3
    caminho_bfs = bfs.path_to(t)
    print("3. Caminho BFS:",
          " -> ".join(estados[v] for v in caminho_bfs) if caminho_bfs else "Não existe")

    # 4 (sem origem)
    alcancaveis = [estados[i] for i in range(g.V) if dfs.marked[i] and i != s]
    print("4. Estados alcançáveis:", ", ".join(alcancaveis))

    # 5
    print("5. Ordem DFS:",
          " -> ".join(estados[v] for v in dfs_order(g, s)))

    # 6
    print("6. Ordem BFS:",
          " -> ".join(estados[v] for v in bfs_order(g, s)))


if __name__ == "__main__":
    main()