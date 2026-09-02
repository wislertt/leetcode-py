def run_minimum_semesters(solution_class: type, n: int, relations: list[list[int]]):
    implementation = solution_class()
    return implementation.minimum_semesters(n, relations)


def assert_minimum_semesters(result: int, expected: int) -> bool:
    assert result == expected
    return True
