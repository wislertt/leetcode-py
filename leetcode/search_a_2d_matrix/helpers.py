def run_search_matrix(solution_class: type, matrix: list[list[int]], target: int):
    implementation = solution_class()
    return implementation.search_matrix(matrix, target)


def assert_search_matrix(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
