def run_kth_smallest(solution_class: type, matrix: list[list[int]], k: int):
    implementation = solution_class()
    return implementation.kth_smallest(matrix, k)


def assert_kth_smallest(result: int, expected: int) -> bool:
    assert result == expected
    return True
