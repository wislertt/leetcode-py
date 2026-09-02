def run_second_minimum(
    solution_class: type, n: int, edges: list[list[int]], time: int, change: int
):
    implementation = solution_class()
    return implementation.second_minimum(n, edges, time, change)


def assert_second_minimum(result: int, expected: int) -> bool:
    assert result == expected
    return True
