def run_magical_string(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.magical_string(n)


def assert_magical_string(result: int, expected: int) -> bool:
    assert result == expected
    return True
