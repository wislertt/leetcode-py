def run_judge_circle(solution_class: type, moves: str):
    implementation = solution_class()
    return implementation.judge_circle(moves)


def assert_judge_circle(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
