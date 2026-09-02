def run_max_len(solution_class: type, arr: list[str]):
    implementation = solution_class()
    return implementation.max_len(arr)


def assert_max_len(result: int, expected: int) -> bool:
    assert result == expected
    return True
