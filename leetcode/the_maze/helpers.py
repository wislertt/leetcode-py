def run_has_path(
    solution_class: type, maze: list[list[int]], start: list[int], destination: list[int]
):
    implementation = solution_class()
    return implementation.has_path(maze, start, destination)


def assert_has_path(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
