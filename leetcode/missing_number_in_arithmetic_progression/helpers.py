def run_missing_number(solution_class: type, arr: list[int]):
    implementation = solution_class()
    return implementation.missing_number(arr)


def assert_missing_number(result: int, expected: int) -> bool:
    assert result == expected
    return True
