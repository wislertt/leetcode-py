def run_best_team_score(solution_class: type, scores: list[int], ages: list[int]):
    implementation = solution_class()
    return implementation.best_team_score(scores, ages)


def assert_best_team_score(result: int, expected: int) -> bool:
    assert result == expected
    return True
