def run_multiply(solution_class: type, mat1: list[list[int]], mat2: list[list[int]]):
    implementation = solution_class()
    return implementation.multiply(mat1, mat2)


def assert_multiply(result: list[list[int]], expected: list[list[int]]) -> bool:
    assert result == expected
    return True
