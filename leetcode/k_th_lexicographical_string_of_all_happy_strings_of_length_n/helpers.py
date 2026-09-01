def run_get_happy_string(solution_class: type, n: int, k: int):
    implementation = solution_class()
    return implementation.get_happy_string(n, k)


def assert_get_happy_string(result: str, expected: str) -> bool:
    assert result == expected
    return True
