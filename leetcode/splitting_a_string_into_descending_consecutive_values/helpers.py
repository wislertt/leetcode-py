def run_split_string(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.split_string(s)


def assert_split_string(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
