def run_colored_cells(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.colored_cells(n)


def assert_colored_cells(result: int, expected: int) -> bool:
    assert result == expected
    return True
