def run_is_self_crossing(solution_class: type, distance: list[int]):
    implementation = solution_class()
    return implementation.is_self_crossing(distance)


def assert_is_self_crossing(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
