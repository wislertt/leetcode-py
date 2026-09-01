def run_maximum_removals(solution_class: type, s: str, p: str, removable: list[int]):
    implementation = solution_class()
    return implementation.maximum_removals(s, p, removable)


def assert_maximum_removals(result: int, expected: int) -> bool:
    assert result == expected
    return True
