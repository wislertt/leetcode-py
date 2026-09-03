def run_has_group_size_x(solution_class: type, deck: list[int]):
    implementation = solution_class()
    return implementation.has_group_size_x(deck)


def assert_has_group_size_x(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
