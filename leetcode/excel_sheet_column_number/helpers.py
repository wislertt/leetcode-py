def run_title_to_number(solution_class: type, column_title: str):
    implementation = solution_class()
    return implementation.title_to_number(column_title)


def assert_title_to_number(result: int, expected: int) -> bool:
    assert result == expected
    return True
