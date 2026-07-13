def run_makesquare(solution_class: type, matchsticks: list[int]):
    implementation = solution_class()
    return implementation.makesquare(matchsticks)


def assert_makesquare(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
