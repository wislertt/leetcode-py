def run_min_add_to_make_valid(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.min_add_to_make_valid(s)


def assert_min_add_to_make_valid(result: int, expected: int) -> bool:
    assert result == expected
    return True
