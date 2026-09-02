def run_count_odds(solution_class: type, low: int, high: int):
    implementation = solution_class()
    return implementation.count_odds(low, high)


def assert_count_odds(result: int, expected: int) -> bool:
    assert result == expected
    return True
