def run_judge_square_sum(solution_class: type, c: int):
    implementation = solution_class()
    return implementation.judge_square_sum(c)


def assert_judge_square_sum(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
