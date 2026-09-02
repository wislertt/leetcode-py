def run_find_lucky(solution_class: type, arr: list[int]):
    implementation = solution_class()
    return implementation.find_lucky(arr)


def assert_find_lucky(result: int, expected: int) -> bool:
    assert result == expected
    return True
