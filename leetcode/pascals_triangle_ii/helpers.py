def run_get_row(solution_class: type, row_index: int):
    implementation = solution_class()
    return implementation.get_row(row_index)


def assert_get_row(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
