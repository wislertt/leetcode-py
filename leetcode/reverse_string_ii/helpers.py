def run_reverse_str(solution_class: type, s: str, k: int):
    implementation = solution_class()
    return implementation.reverse_str(s, k)


def assert_reverse_str(result: str, expected: str) -> bool:
    assert result == expected
    return True
