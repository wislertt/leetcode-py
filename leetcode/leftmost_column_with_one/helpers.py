from .solution import BinaryMatrix


def run_leftmost_column_with_one(solution_class: type, mat: list[list[int]]):
    binary_matrix = BinaryMatrix(mat)
    result = solution_class().leftmost_column_with_one(binary_matrix)
    return result, binary_matrix.calls


def assert_leftmost_column_with_one(result: tuple[int, int], expected: int) -> bool:
    assert result[0] == expected
    assert result[1] <= 1000
    return True
