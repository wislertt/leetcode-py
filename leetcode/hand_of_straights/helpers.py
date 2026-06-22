def run_is_n_straight_hand(solution_class: type, hand: list[int], group_size: int):
    implementation = solution_class()
    return implementation.is_n_straight_hand(hand, group_size)


def assert_is_n_straight_hand(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
