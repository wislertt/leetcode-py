def run_min_number_operations(solution_class: type, target: list[int]):
    implementation = solution_class()
    return implementation.min_number_operations(target)


def assert_min_number_operations(result: int, expected: int) -> bool:
    assert result == expected
    return True
