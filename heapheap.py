import random
#import heapq
random.seed('class_02')

def downHeap(arr, root, size):
    lc = root * 2 + 1
    if lc >= size: return
    child = lc

    rc = lc + 1
    if rc < size:
        if arr[rc] > arr[lc]:
            child = rc

    if arr[root] >= arr[child]: return

    arr[root], arr[child] = arr[child], arr[root]
    downHeap(arr, child, size)

array = [ random.randrange(100) for _ in range(30)]
l_arr = len(array)
#heapq.heapify(array)
for i in range(l_arr // 2 - 1, -1, -1):
    downHeap(array, i, l_arr)
print(array)

for i in range(l_arr - 1, 0, -1):
    array[0], array[i] = array[i], array[0]
    l_arr -= 1
    downHeap(array, 0, l_arr)
    print(array)