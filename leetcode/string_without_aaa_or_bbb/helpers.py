def run_str_without3a3b(solution_class: type, a: int, b: int):
    implementation = solution_class()
    return implementation.str_without3a3b(a, b)


def assert_str_without3a3b(result: str, expected: int) -> bool:
    # Any valid string is accepted; expected is the required length a + b
    assert len(result) == expected
    assert "aaa" not in result
    assert "bbb" not in result
    return True
