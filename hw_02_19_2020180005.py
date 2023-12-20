import random

random.seed('class_02')
n_pts = 100
n_cluster = 6

class Point:
    def __init__(self):
        self.x = random.randint(1, 1000)
        self.y = random.randint(1, 1000)

    def __repr__(self):
        return f'({self.x}, {self.y})'

pts = [Point() for _ in range(n_pts)]
print(pts)

from heapdict import heapdict
D = heapdict() # (-distance, k_th_center_index)
C = [] # centers


def distance_sq_between(i1, i2):
    p1, p2 = pts[i1], pts[i2]
    return (p1.x - p2.x)**2 + (p1.y - p2.y)**2


for k in range(n_cluster):
    # k번째 center를 결정한다
    if k == 0: # 첫번째이면
        center = random.randrange(n_pts)
    else:
        # center = D.popitem()[0] #(i, (v, i2))
        center, _ = D.popitem()
    # center = D.popitem()[0] if k > 0 else random.randrange(n_pts)

    # 이번에 추가된 센터를 기록한다
    C.append(center)
    D[center] = (0, k)

    # 모든 점에 대해 거리갱신을 (필요하면) 합니다
    for i in range(n_pts):
        # 방금 추가된 센터까지의 거리를 구해서
        d = distance_sq_between(center, i)
        # dists 딕셔너리에 갱신해준다
        if not i in D or d < -D[i][0]:
            D[i] = (-d, k)
            # Min-Heap이므로 음수로 기록해야 최대값을 얻을 수 있으며,
            # 가까운 센터가 몇번째 센터인지도 함께 저장한다

clusters = [ [] for _ in range(n_cluster) ]
# n_clusters 개수 만큼 빈 배열을 준비한다
for i in range(n_pts): #모든 점들에 대하여
    #정점 i가 몇번째 center 와 가까운지 알아내자
    ci = D[i][1]
    #_, ci = D[i]
    clusters[ci].append(pts[i])

print(clusters)

from welzl import welzl
# 제일 큰 원의 반지름을 max_r에 저장한다
max_r = 0
for ci in range(n_cluster):
    x, y, r = welzl(clusters[ci]) # 반지름 r을 구한다
    max_r = max(max_r, r)

print(f'Max R = {round(max_r)}')