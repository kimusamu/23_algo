import random
import math
random.seed('class_02')
array = [random.randrange(100000) for _ in range(30)]
maxv = max(array)
radix_count = math.ceil(math.log10(maxv + 1))
l_arr = len(array)
results = [0 for _ in range(l_arr)]
div = 1
for r in range(radix_count):
    counts = [0 for _ in range(10)]
    for n in array:
        digit = n // div % 10
        counts[digit] += 1

    for i in range(10 - 1):
        counts[i + 1] += counts[i]

    for i in range(l_arr - 1, -1, -1):
        v = array[i]
        digit = v // div % 10
        counts[digit] -= 1
        ri = counts[digit]
        results[ri] = v

    array = results[:]
    print(results)
    div *= 10

#print(array)
#print(maxv, radix_count)
exit()








print(counts)
for n in array:
    counts[n] += 1
print(counts)

for i in range(10 - 1):
    counts[i + 1] += counts[i]
print(counts)

results = [0 for _ in range(l_arr)]

for i in range(l_arr - 1, -1, -1):
    v = array[i]
    counts[v] -= 1
    ri = counts[v]
    results[ri] = v
    print(results)