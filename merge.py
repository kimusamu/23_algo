import random
random.seed('class_02')
array = [random.randrange(100) for _ in range(30)]
l_arr = len(array)
print(array, l_arr)


# mid is in left
# end is inclusive
def merge(arr, beg, mid, end):
    merged = []
    l, r = beg, mid + 1
    while l <= mid and r <= end:
        if arr[l] <= arr[r]:
            merged.append(arr[l])
            l += 1
        else:
            merged.append(arr[r])
            r += 1
    while l <= mid:
        merged.append(arr[l])
        l += 1
    while r <= end:
        merged.append(arr[r])
        r += 1

    arr[beg : end + 1] = merged


# end: inclusive
def mergeSort(arr, beg, end):
    if beg >= end:   
        return
    
    mid = (beg + end) // 2 # mid is in left
    mergeSort(arr, beg, mid)
    mergeSort(arr, mid + 1, end)
    merge(arr, beg, mid, end)
    print(arr)


mergeSort(array, 0, l_arr - 1)
