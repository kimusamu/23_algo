def matrix_chain_order(d):
    n = len(d) - 1  # 행렬 개수
    m = [[0] * n for _ in range(n)]  # 최적의 곱셈 순서를 저장하는 행렬
    s = [[0] * n for _ in range(n)]  # 최적의 괄호 위치를 저장하는 행렬

    # 행렬 하나만 있는 경우
    for i in range(n):
        m[i][i] = 0

    # chain length은 2부터 n까지 증가
    for chain_length in range(2, n + 1):
        for i in range(n - chain_length + 1):
            j = i + chain_length - 1
            m[i][j] = float('inf')  # 무한대로 초기화

            # 가능한 모든 괄호 위치에 대해 최소 곱셈 비용 계산
            for k in range(i, j):
                cost = m[i][k] + m[k + 1][j] + d[i] * d[k + 1] * d[j + 1]
                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k

    return m, s

def print_optimal_parenthesis(s, i, j):
    if i == j:
        print(f'M{str(i)}', end='')
    else:
        print('(', end='')
        print_optimal_parenthesis(s, i, s[i][j])
        print(" x ", end='')
        print_optimal_parenthesis(s, s[i][j] + 1, j)
        print(')', end='')

d = [2, 8, 2, 9, 8, 3, 9, 2]
m, s = matrix_chain_order(d)

print("Optimal Parenthesization:")
print_optimal_parenthesis(s, 0, len(d) - 2)
print("\nMinimum number of multiplications:", m[0][-1])