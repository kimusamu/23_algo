from data_unsorted import numbers

#입력 : 입력이 arr[1]부터 arr[n]까지 저장된 배열 A
#출력 : 정렬된 배열 arr

def downheap(arr, size, idx):
    largest = idx # 현재 노드를 가장 큰 값으로 설정
    left_child = 2 * idx + 1 # 왼쪽 자식 노드 인덱스 계산
    right_child = 2 * idx + 2 # 오른쪽 자식 노드 인덱스 계산

    # 왼쪽 자식이 힙 크기 내에 있고 현재 노드보다 큰 경우
    if left_child < size and arr[left_child] > arr[largest]:
        largest = left_child

    # 오른쪽 자식이 힙 크기 내에 있고 현재 노드나 왼쪽 자식보다 큰 경우
    if right_child < size and arr[right_child] > arr[largest]:
        largest = right_child

    # 현재 노드가 가장 큰 노드가 아니면 교환
    if largest != idx:
        arr[idx], arr[largest] = arr[largest], arr[idx]

        # 변경된 노드를 대상으로 재귀적으로 downheap을 호출
        downheap(arr, size, largest)

#배열 arr의 숫자에 대해서 힙 자료 구조를 만든다
def heapify(arr):
    size = len(arr)
    for i in range(size // 2 - 1, -1, -1):
        downheap(arr, size, i)

def heap_sort(numbers):
    print('before : ', numbers)

    heapify(numbers)

    size = len(numbers) - 1 #힙의 크기를 조절하는 변수

    for i in range(size, 0, -1):  # 변경된 부분
        numbers[0], numbers[i] = numbers[i], numbers[0]
        downheap(numbers, i, 0)

    print('after : ', numbers)

#heap_sort(numbers)

#------------------------------------------------------------------------------
#기수정렬
#입력 : n개의 r진수의 k자리 숫자
#출력 : 정렬된 숫자

def radix_sort(numbers, n, k, r):
    print('before : ', numbers)

    def counting_sort(numbers, exp):
        count = [0] * r
        output = [0] * n

        for i in range(n):
            index = (numbers[i] // exp) % r
            count[index] += 1

        for i in range(1, r):
            count[i] += count[i - 1]

        i = n - 1

        while i >= 0:
            index = (numbers[i] // exp) % r
            output[count[index] - 1] = numbers[i]
            count[index] -= 1
            i -= 1

        for i in range(n):
            numbers[i] = output[i]

    for i in range(k):
        exp = r ** i
        counting_sort(numbers, exp)

    print('after : ', numbers)

radix_sort(numbers, 100, 10, 3)