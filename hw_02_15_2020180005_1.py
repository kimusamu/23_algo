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

def floyd_warshall(edges, num_vertex):
    # 초기화
    inf = float('inf')
    dist = [[inf] * num_vertex for _ in range(num_vertex)]
    next_vertex = [[None] * num_vertex for _ in range(num_vertex)]

    for edge in edges:
        src, dest, cost = edge
        dist[src][dest] = cost
        next_vertex[src][dest] = dest

    for i in range(num_vertex):
        dist[i][i] = 0

    for k in range(num_vertex):
        for i in range(num_vertex):
            for j in range(num_vertex):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_vertex[i][j] = next_vertex[i][k]

    for i in range(num_vertex):
        for j in range(num_vertex):
            if i != j and next_vertex[i][j] is not None:
                path = reconstruct_path(i, j, next_vertex)
                print(f"Path from {i} to {j}: {path}, Cost: {dist[i][j]}")

def reconstruct_path(start, end, next_vertex):
    path = [start]
    while start != end:
        start = next_vertex[start][end]
        path.append(start)
    return path

floyd_warshall(edges, num_vertex)
