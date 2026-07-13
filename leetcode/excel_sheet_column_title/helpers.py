def run_convert_to_title(solution_class: type, column_number: int):
    implementation = solution_class()
    return implementation.convert_to_title(column_number)


def assert_convert_to_title(result: str, expected: str) -> bool:
    assert result == expected
    return True
