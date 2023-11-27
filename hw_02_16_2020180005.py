from random import randint
from heapdict import heapdict

edges = [
      (0, 6, 130), (0, 17, 280), (0, 19, 435), (1, 4, 449), (1, 5, 392),
      (1, 7, 346), (1, 13, 325), (2, 21, 335), (3, 6, 231), (3, 17, 140),
      (3, 20, 323), (4, 5, 390), (4, 12, 299), (4, 15, 399), (5, 10, 445),
      (5, 13, 234), (6, 12, 468), (6, 16, 377), (6, 17, 168), (6, 19, 304),
      (6, 21, 309), (7, 12, 362), (7, 13, 288), (7, 21, 445), (8, 9, 230),
      (8, 18, 103), (9, 11, 314), (9, 16, 323), (9, 17, 439), (9, 18, 154),
      (10, 13, 328), (10, 15, 207), (10, 21, 433), (11, 14, 226), (11, 15, 381),
      (11, 18, 444), (11, 19, 378), (11, 20, 113), (12, 13, 264), (12, 15, 402),
      (12, 19, 346), (14, 15, 320), (14, 19, 454), (14, 20, 326), (15, 19, 243),
      (16, 17, 308), (17, 20, 293),
]

num_vertex = 22

D = heapdict()
completed = set()
origins = dict()
start_index = 1

D[start_index] = 0, start_index
origins[start_index] = start_index

mst_edges = []
seq = [start_index]

def build_graph(edges):
    g = {u: dict() for u in range(num_vertex)}
    for u, v, w in edges:
        g[u][v] = w
        g[v][u] = w
    return g

def mst():
    while D:
        v, w = D.popitem()
        u = origins[v]
        if u != v:
            mst_edges.append((u, v, w))
            completed.add(v)
        for adj, weight in g[v].items():
            if adj in completed: continue
            if adj in D and D[adj] < weight: continue
            D[adj] = weight
            origins[adj] = v

def make_sequence():
    current = start_index

    while True:
        if current == start_index and not mg[start_index]:
            break
        adjs = mg[current].keys()
        visit = None
        for k in adjs:
            if visit == None: visit = k
            if k not in seq:
                visit = k
                break
        mg[current].pop(visit)
        seq.append(visit)
        current = visit

def find_shortcut():
    visited = set()
    index = 0
    while index < len(seq):
        current = seq[index]
        if current in visited:
            seq.pop(index)
        else:
            visited.add(current)
            index += 1
    seq.append(start_index)

def tsp():
    make_sequence()
    print(seq)
    find_shortcut()
    print(seq)

g = build_graph(edges)
mst()
mg = build_graph(mst_edges)
tsp()

