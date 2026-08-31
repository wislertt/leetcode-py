def run_is_one_edit_distance(solution_class: type, s: str, t: str):
    implementation = solution_class()
    return implementation.is_one_edit_distance(s, t)


def assert_is_one_edit_distance(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
