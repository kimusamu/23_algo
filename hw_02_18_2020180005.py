import random

random.seed('class_02')
BIN_SIZE = 50
nums = [random.randint(1, 10) for _ in range(30)]
print(nums)

bins = []

def free(b):
    s = 0
    for n in b:
        s += n
    return BIN_SIZE - s

def hasSize(b, num):
    return free(b) >= num

def first_fit(n):
    for b in bins:
        if hasSize(b, n):
            return b
    b = []
    bins.append(b)
    return b

last_bin = None
def next_fit(n):
    global last_bin
    if last_bin != None and hasSize(last_bin, n):
        return last_bin
    last_bin = []
    bins.append(last_bin)
    return last_bin

def best_fit(n):
    smallest = (None, BIN_SIZE)
    for b in bins:
        f = free(b)
        if f < n or f >= smallest[1]: continue
        smallest = b, f
    if smallest[0] != None:
        return smallest[0]
    b = []
    bins.append(b)
    return b

def worst_fit(n):
    largest = (None, 0)  # Initialize largest with 0 free space
    for b in bins:
        f = free(b)
        if f >= n and f > largest[1]:
            largest = b, f
    if largest[0] != None:
        return largest[0]
    b = []
    bins.append(b)
    return b

for fit in [ first_fit, next_fit, best_fit, worst_fit ]:
    bins = []
    print(fit)
    for n in nums:
        b = fit(n)
        b.append(n)
    print(bins)