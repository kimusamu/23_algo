from data_unsorted import numbers

#입력 : 입력이 arr[1]부터 arr[n]까지 저장된 배열 A
#출력 : 정렬된 배열 arr

def heapify(root, size):
    lc = root * 2 + 1 # lc = Left Child 

    if lc >= size: # child 가 없다는 의미이다
        return
    
    child = lc
    rc = root * 2 + 2 # rc = Right Child 

    if rc < size: # lc 만 있을 수도 있지만, rc 도 있다면
        if numbers[rc] > numbers[lc]: # lc 와 rc 중 큰 것을 비교하여
            child = rc # child 에 담는다

    if numbers[root] < numbers[child]: # parent 와 child 중에 어느것이 큰지 비교하여
        numbers[root], numbers[child] = numbers[child], numbers[root] # 필요시 교체한다
        heapify(child, size) # 교체되어 내려간 child 를 새로운 parent 로 하여 재귀 호출한다

def heap_sort(numbers):
    print('before : ', numbers)
    count = len(numbers)

    last_parent_index = count // 2 - 1

    for n in range(last_parent_index, -1, -1):
        heapify(n, count)

    last_parent_index = count - 1

    while last_parent_index > 0:
        numbers[0], numbers[last_parent_index] = numbers[last_parent_index], numbers[0] # 첫번째와 마지막의 원소를 교환한다
        heapify(0, last_parent_index) # Root 에 새로운 녀석이 들어왔으므로 Heap 이 되기 위해 내린다
        last_parent_index -= 1

    print('after : ', numbers)

heap_sort(numbers)

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

            #현재 자릿수부터 가장 큰 자릿수까지 반복적으로 수행되어 전체 숫자배열 정렬
            #핵심은 각 숫자의 등장횟수를 세어서 정렬 수행, 누적 등장 횟수를 이용하여 숫자들을 정렬된 위치에 배치하는 것
            #계수 정렬은 숫자범위가 제한적일때 가장 효율적으로 작동하며, 비교기간 정렬과는 다른 원리를 가짐

    for i in range(k): #자릿수를 계속해서 넘어간다
        exp = r ** i # **은 r의 i제곱을 의미함, 제곱을 통해서 자릿수가 넘어감
        counting_sort(numbers, exp)

    print('after : ', numbers)

#radix_sort(numbers, 100, 10, 3)