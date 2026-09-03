def run_escape_ghosts(solution_class: type, ghosts: list[list[int]], target: list[int]):
    implementation = solution_class()
    return implementation.escape_ghosts(ghosts, target)


def assert_escape_ghosts(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
