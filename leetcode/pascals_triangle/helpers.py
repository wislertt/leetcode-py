def run_generate(solution_class: type, num_rows: int):
    implementation = solution_class()
    return implementation.generate(num_rows)


def assert_generate(result: list[list[int]], expected: list[list[int]]) -> bool:
    assert result == expected
    return True
