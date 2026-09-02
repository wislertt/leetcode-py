def run_has_all_codes(solution_class: type, s: str, k: int):
    implementation = solution_class()
    return implementation.has_all_codes(s, k)


def assert_has_all_codes(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
