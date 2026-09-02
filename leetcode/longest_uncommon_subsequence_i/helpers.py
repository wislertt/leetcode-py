def run_find_luslength(solution_class: type, a: str, b: str):
    implementation = solution_class()
    return implementation.find_luslength(a, b)


def assert_find_luslength(result: int, expected: int) -> bool:
    assert result == expected
    return True
