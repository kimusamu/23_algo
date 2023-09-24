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

    def counting_sort(numbers, exp): #해당 자릿수에서 정렬을 실시한다
        count = [0] * r #카운트 배열 초기화, 각 숫자의 등장횟수 저장
        output = [0] * n #결과 배열 초기화, 정렬된 결과를 저장할 배열

        for i in range(n): #리스트를 순회하여, 각 숫자가 현재 자릿수에서 얼마인지 기록, 등장횟수는 count에 기록
            index = (numbers[i] // exp) % r
            count[index] += 1

        for i in range(1, r): #count배열을 통해 누적 등장 횟수 계산, 이를 통해 각 숫자가 정렬된 배열에서 어느 위치에 위치해야하는지 알 수 있음
            count[i] += count[i - 1]

        i = n - 1

        while i >= 0: #numbers리스트 역순하여 각 숫자를 현재 자릿수에 맞게 output 배열 배치, 해당 숫자 누적 등장 횟수 1 감소
            index = (numbers[i] // exp) % r
            output[count[index] - 1] = numbers[i]
            count[index] -= 1
            i -= 1

        for i in range(n): #output 배열 저장 후 다시 numbers 배열로 복사
            numbers[i] = output[i]

    for i in range(k): #자릿수를 계속해서 넘어간다
        exp = r ** i # **은 r의 i제곱을 의미함, 제곱을 통해서 자릿수가 넘어감
        counting_sort(numbers, exp)

    print('after : ', numbers)

radix_sort(numbers, 100, 10, 3)