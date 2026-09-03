def run_number_of_lines(solution_class: type, widths: list[int], s: str):
    implementation = solution_class()
    return implementation.number_of_lines(widths, s)


def assert_number_of_lines(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
