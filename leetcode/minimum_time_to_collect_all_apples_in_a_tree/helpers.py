def run_min_time(solution_class: type, n: int, edges: list[list[int]], has_apple: list[bool]):
    implementation = solution_class()
    return implementation.min_time(n, edges, has_apple)


def assert_min_time(result: int, expected: int) -> bool:
    assert result == expected
    return True
