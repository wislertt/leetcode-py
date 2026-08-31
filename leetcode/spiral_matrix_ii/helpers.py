def run_generate_matrix(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.generate_matrix(n)


def assert_generate_matrix(result: list[list[int]], expected: list[list[int]]) -> bool:
    assert result == expected
    return True
