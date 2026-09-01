def run_max_score(solution_class: type, card_points: list[int], k: int):
    implementation = solution_class()
    return implementation.max_score(card_points, k)


def assert_max_score(result: int, expected: int) -> bool:
    assert result == expected
    return True
