def run_lemonade_change(solution_class: type, bills: list[int]):
    implementation = solution_class()
    return implementation.lemonade_change(bills)


def assert_lemonade_change(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
