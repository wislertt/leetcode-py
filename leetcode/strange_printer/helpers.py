def run_strange_printer(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.strange_printer(s)


def assert_strange_printer(result: int, expected: int) -> bool:
    assert result == expected
    return True
