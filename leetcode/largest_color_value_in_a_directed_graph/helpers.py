def run_largest_path_value(solution_class: type, colors: str, edges: list[list[int]]):
    implementation = solution_class()
    return implementation.largest_path_value(colors, edges)


def assert_largest_path_value(result: int, expected: int) -> bool:
    assert result == expected
    return True
