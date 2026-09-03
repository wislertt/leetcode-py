def run_reach_number(solution_class: type, target: int):
    implementation = solution_class()
    return implementation.reach_number(target)


def assert_reach_number(result: int, expected: int) -> bool:
    assert result == expected
    return True
