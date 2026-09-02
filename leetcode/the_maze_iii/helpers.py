def run_find_shortest_way(
    solution_class: type, maze: list[list[int]], ball: list[int], hole: list[int]
):
    implementation = solution_class()
    return implementation.find_shortest_way(maze, ball, hole)


def assert_find_shortest_way(result: str, expected: str) -> bool:
    assert result == expected
    return True
