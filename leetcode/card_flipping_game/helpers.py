def run_flipgame(solution_class: type, fronts: list[int], backs: list[int]):
    implementation = solution_class()
    return implementation.flipgame(fronts, backs)


def assert_flipgame(result: int, expected: int) -> bool:
    assert result == expected
    return True
