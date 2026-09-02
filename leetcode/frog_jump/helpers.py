def run_can_cross(solution_class: type, stones: list[int]):
    implementation = solution_class()
    return implementation.can_cross(stones)


def assert_can_cross(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
