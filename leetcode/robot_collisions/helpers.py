def run_survived_robots_healths(
    solution_class: type, positions: list[int], healths: list[int], directions: str
):
    implementation = solution_class()
    return implementation.survived_robots_healths(positions, healths, directions)


def assert_survived_robots_healths(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
