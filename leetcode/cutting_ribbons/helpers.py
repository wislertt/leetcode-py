def run_max_length(solution_class: type, ribbons: list[int], k: int):
    implementation = solution_class()
    return implementation.max_length(ribbons, k)


def assert_max_length(result: int, expected: int) -> bool:
    assert result == expected
    return True
