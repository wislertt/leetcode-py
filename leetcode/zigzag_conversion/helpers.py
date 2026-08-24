def run_convert(solution_class: type, s: str, num_rows: int):
    implementation = solution_class()
    return implementation.convert(s, num_rows)


def assert_convert(result: str, expected: str) -> bool:
    assert result == expected
    return True
