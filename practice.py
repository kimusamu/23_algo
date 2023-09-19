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
        to_insert = numbers[end]
        i = end
        while i > 0 and numbers[i - 1] > to_insert:
            numbers[i] = numbers[i - 1]
            i -= 1
        numbers[i] = to_insert

    print('after : ', numbers)

def shell_sort(numbers):
    print('before : ', numbers)

    for h in range(10, 1, -1):
        for i in range(h, len(numbers) - 1):
            currentelement = numbers[i]
            j = i
            while(j >= h and numbers[j - h] > currentelement):
                numbers[j] = numbers[j - h]
                j = j - h
            numbers[j] = currentelement

    print('after : ', numbers)


#bubble_sort(numbers)
#selection_sort(numbers)
#insertion_sort(numbers)
shell_sort(numbers)

