def run_length_longest_path(solution_class: type, input_str: str):
    implementation = solution_class()
    return implementation.length_longest_path(input_str)


def assert_length_longest_path(result: int, expected: int) -> bool:
    assert result == expected
    return True
