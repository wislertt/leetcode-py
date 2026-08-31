def run_max_score_sightseeing_pair(solution_class: type, values: list[int]):
    implementation = solution_class()
    return implementation.max_score_sightseeing_pair(values)


def assert_max_score_sightseeing_pair(result: int, expected: int) -> bool:
    assert result == expected
    return True
