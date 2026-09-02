def run_matrix_reshape(solution_class: type, mat: list[list[int]], r: int, c: int):
    implementation = solution_class()
    return implementation.matrix_reshape(mat, r, c)


def assert_matrix_reshape(result: list[list[int]], expected: list[list[int]]) -> bool:
    assert result == expected
    return True
