def run_max_number_of_apples(solution_class: type, weight: list[int]):
    implementation = solution_class()
    return implementation.max_number_of_apples(weight)


def assert_max_number_of_apples(result: int, expected: int) -> bool:
    assert result == expected
    return True
