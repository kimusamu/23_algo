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


class Floyd:
    print('[Floyd Warshall]')
    INF = float('inf')
    dgraph = {}
    dirs = {}

    def __init__(self, num_vertex):
        self.num_vertex = num_vertex
        for u in range(self.num_vertex):
            self.dgraph[u] = {}
            self.dirs[u] = {}
            for v in range(self.num_vertex):
                if any(x == (u, v) for x in edges):
                    idx = edges.index((u, v))
                    self.dgraph[u][v] = edges[idx][2]
                    self.dirs[u][v] = v
                else:
                    self.dgraph[u][v] = self.INF
                    self.dirs[u][v] = -1
            self.dgraph[u][u] = 0

    def start(self):
        for k in range(self.num_vertex):
            for i in range(self.num_vertex):
                for j in range(self.num_vertex):
                    dist = self.dgraph[i][j]
                    via = self.dgraph[i][k] + self.dgraph[k][j]
                    if via < dist:
                        self.dgraph[i][j] = via
                        self.dirs[i][j] = k

    def print_paths(self):
        for i in range(self.num_vertex):
            for j in range(self.num_vertex):
                path = [i]
                if i != j:
                    k = self.dirs[i][j]
                    while k != -1:
                        path.append(k)
                        if k == j:
                            break
                        k = self.dirs[k][j]

                path = ' -> '.join(map(str, path))
                print(f"Path from {i} to {j}: {path}")


floyd = Floyd(num_vertex)
floyd.start()
floyd.print_paths()