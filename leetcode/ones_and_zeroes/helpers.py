def run_find_max_form(solution_class: type, strs: list[str], m: int, n: int):
    implementation = solution_class()
    return implementation.find_max_form(strs, m, n)


def assert_find_max_form(result: int, expected: int) -> bool:
    assert result == expected
    return True
