from random import randint

class ChainedMatrixMult:
    print('[Chained Matrix Multiplication]')
    def __init__(self, sizes):
        self.sizes = sizes
        self.matrix_count = len(self.sizes) - 1
        self.matrices = [self.generate_matrix(self.sizes[i], self.sizes[i + 1]) for i in range(self.matrix_count)]
        self.C = [[0 for _ in range(self.matrix_count)] for _ in range(self.matrix_count)]
        self.P = [[0 for _ in range(self.matrix_count)] for _ in range(self.matrix_count)]

    def generate_matrix(self, rows, columns):
        return [[randint(1, 10) for _ in range(columns)] for _ in range(rows)]

    def matrix_chain_order(self):
        for length in range(2, self.matrix_count + 1):
            for i in range(self.matrix_count - length + 1):
                j = i + length - 1
                self.C[i][j] = float('inf')
                for k in range(i, j):
                    cost = self.C[i][k] + self.C[k + 1][j] + self.sizes[i] * self.sizes[k + 1] * self.sizes[j + 1]
                    if cost < self.C[i][j]:
                        self.C[i][j] = cost
                        self.P[i][j] = k

    def print_matrices(self):
        for i, matrix in enumerate(self.matrices):
            print(f"Matrix {i}:")
            for row in matrix:
                print(row)
            print()

    def print_optimal_parentheses(self, i, j):
        if i == j:
            print(f"M{i}", end="")
        else:
            print("(", end="")
            self.print_optimal_parentheses(i, self.P[i][j])
            print(" x ", end="")
            self.print_optimal_parentheses(self.P[i][j] + 1, j)
            print(")", end="")

    def get_minimum_cost(self):
        return self.C[0][self.matrix_count - 1]


d = [2, 3, 4, 2, 5, 6, 2, 8]
cm = ChainedMatrixMult(d)
#cm.print_matrices()
cm.matrix_chain_order()
print("\nOptimal Parenthesization: ", end="")
cm.print_optimal_parentheses(0, len(d) - 2)
print()
print("Minimum cost:", cm.get_minimum_cost())
