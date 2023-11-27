from random import randrange


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

adjs = [set() for _ in range(num_vertex)]

for i in range(len(edges)):
      u, v, w = edges[i]
      adjs[u].add(v)
      adjs[v].add(u)

vc = set()
edge_count = 0
vertices = list(range(num_vertex))

while edge_count < len(edges):
      vi = randrange(len(vertices))
      u = vertices.pop(vi)
      if not adjs[u]: continue
      v = adjs[u].pop()

      for n in (u, v):
            vc.add(n)
            for k in range(num_vertex):
                  if k in adjs[n]:
                        adjs[n].remove(k)
                        if n in adjs[k]:
                              adjs[k].remove(n)
                        edge_count += 1

      print(f'vc={vc}')