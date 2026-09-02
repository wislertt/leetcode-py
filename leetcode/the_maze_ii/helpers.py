def run_shortest_distance(
    solution_class: type, maze: list[list[int]], start: list[int], destination: list[int]
):
    implementation = solution_class()
    return implementation.shortest_distance(maze, start, destination)


def assert_shortest_distance(result: int, expected: int) -> bool:
    assert result == expected
    return True
