import random
random.seed('class_02')
array = [random.randrange(100) for _ in range(30)]
l_arr = len(array)
#print(array, l_arr)


def partition(arr, beg, end):
    ri = random.randrange(beg, end) # randint(beg, end - 1)
    arr[beg], arr[ri] = arr[ri], arr[beg]
    pv = arr[beg]
    p, q = beg + 1, end - 1

    while True: # 역전안됐으면
        while True: # 오른쪽으로 보낼애 찾을때까지
            if p >= q: break
            if arr[p] > pv : break
            p += 1
        while True: # 왼쪽으로 보낼애 찾을때까지
            if p > q: break
            if arr[q] <= pv : break
            q -= 1
        if p >= q: break # 역전이 되었다
        
        arr[p], arr[q] = arr[q], arr[p] # 바꾼다
        p += 1
        q -= 1

    arr[q], arr[beg] = arr[beg], arr[q]
    return q


def quickSort(arr, beg, end): # end is exclusive
    if end - beg <= 1 : return

    pi = partition(arr, beg, end)
    quickSort(arr, beg, pi)
    quickSort(arr, pi + 1, end)


quickSort(array, 0, l_arr)
print(array)