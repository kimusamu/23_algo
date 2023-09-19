from data_unsorted import numbers

def bubble_sort(numbers):
    print('before : ', numbers)

    end = len(numbers) - 1

    for a in range(end):
        for b in range(end - a):
            if numbers[b] > numbers[b + 1]:
                numbers[b], numbers[b + 1] = numbers[b + 1], numbers[b]

    print('after : ', numbers)

def selection_sort(numbers):
    print('before : ', numbers)

    for i in range(len(numbers) - 1):
        min_idx = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[min_idx]:
                min_idx = j
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]

    print('after : ', numbers)

def insertion_sort(numbers):
    print('before : ', numbers)

    for end in range(1, len(numbers)):
        for i in range(end, 0, -1):
            if numbers[i - 1] > numbers[i]:
                numbers[i - 1], numbers[i] = numbers[i], numbers[i - 1]

    print('after : ', numbers)

def shell_sort(numbers):
    n = len(numbers)
    h = n // 3

    print('before : ', numbers)

    while(h > 0):
        for i in range(h, n):
            temp = numbers[i]
            j = i - h
            while(j >= 0 and numbers[j] > temp):
                numbers[j + h] = numbers[j]
                j -= h
            numbers[j + h] = temp
        h //= 3

    print('after : ', numbers)


#bubble_sort(numbers)
selection_sort(numbers)
#insertion_sort(numbers)
#shell_sort(numbers)

