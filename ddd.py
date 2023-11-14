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

INF = float('inf')
g = [[INF for _ in range(num_vertex)] for _ in range(num_vertex)]
via = [[-1 for _ in range(num_vertex)] for _ in range(num_vertex)]

for s, e, w in edges:
    g[s][e] = w
    g[e][s] = w
    via[s][e] = e
    via[e][s] = e

#print(g)

for k in range(num_vertex):
    for s in range(num_vertex):
        if s == k: continue
        for e in range(num_vertex):
            if e == k or e == k: continue
            if g[s][k] + g[k][e] < g[s][e]:
                g[s][e] = g[s][k] + g[k][e]
                via[s][e] = k

def get_path(s, e):
    path = [s]
    while s != e:
        k = via[s][e]
        if k == e:
            path.append(e)
        else:
            path.append(k)
        s = k
    return '-'.join(map(str, path))

for s in range(num_vertex):
    for e in range(num_vertex):
        if s == e: continue
        print(str(s) + get_path(s, e))