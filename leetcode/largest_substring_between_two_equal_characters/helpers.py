def run_max_length_between_equal_characters(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.max_length_between_equal_characters(s)


def assert_max_length_between_equal_characters(result: int, expected: int) -> bool:
    assert result == expected
    return True
