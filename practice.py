from data_unsorted import numbers

#입력 : 입력이 arr[1]부터 arr[n]까지 저장된 배열 A
#출력 : 정렬된 배열 arr
#배열 arr의 숫자에 대해서 힙 자료 구조를 만든다

def heap_sort(numbers):
    print(numbers)

    size = len(numbers) - 1 #힙의 크기를 조절하는 변수
    for i in range(1, len(numbers)):
        numbers[1] = numbers[size] #루트와 힙의 마지막 노드를 교환한다
        size = size - 1 #힙의 크기를 1 감소한다
        #downheap() #위배된 힙 조건을 만족시킨다, 다운힙을 따로 만들것

    print(numbers)

heap_sort(numbers)