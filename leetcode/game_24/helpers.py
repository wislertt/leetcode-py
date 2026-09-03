def run_judge_point24(solution_class: type, cards: list[int]):
    implementation = solution_class()
    return implementation.judge_point24(cards)


def assert_judge_point24(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
