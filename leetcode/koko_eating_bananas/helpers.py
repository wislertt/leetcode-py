def run_min_eating_speed(solution_class: type, piles: list[int], h: int):
    implementation = solution_class()
    return implementation.min_eating_speed(piles, h)


def assert_min_eating_speed(result: int, expected: int) -> bool:
    assert result == expected
    return True
