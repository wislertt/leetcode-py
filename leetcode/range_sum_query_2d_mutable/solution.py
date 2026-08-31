class BinaryIndexedTree:
    def __init__(self, n: int) -> None:
        self.n = n
        self.c = [0] * (n + 1)

    @staticmethod
    def lowbit(x: int) -> int:
        return x & -x

    def update(self, x: int, delta: int) -> None:
        while x <= self.n:
            self.c[x] += delta
            x += BinaryIndexedTree.lowbit(x)

    def query(self, x: int) -> int:
        s = 0
        while x > 0:
            s += self.c[x]
            x -= BinaryIndexedTree.lowbit(x)
        return s


class NumMatrix:
    # Time: O(m * n log n) build — one BIT per row
    # Space: O(m * n)
    def __init__(self, matrix: list[list[int]]) -> None:
        self.matrix = matrix
        self.trees = [BinaryIndexedTree(len(row)) for row in matrix]
        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                self.trees[i].update(j + 1, val)

    # Time: O(log n)
    # Space: O(1)
    def update(self, row: int, col: int, val: int) -> None:
        delta = val - self.matrix[row][col]
        self.matrix[row][col] = val
        self.trees[row].update(col + 1, delta)

    # Time: O(m log n)
    # Space: O(1)
    def sum_region(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return sum(
            self.trees[i].query(col2 + 1) - self.trees[i].query(col1) for i in range(row1, row2 + 1)
        )
