def run_find_the_city(
    solution_class: type, n: int, edges: list[list[int]], distance_threshold: int
):
    implementation = solution_class()
    return implementation.find_the_city(n, edges, distance_threshold)


def assert_find_the_city(result: int, expected: int) -> bool:
    assert result == expected
    return True
