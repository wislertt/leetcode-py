def run_num_teams(solution_class: type, rating: list[int]):
    implementation = solution_class()
    return implementation.num_teams(rating)


def assert_num_teams(result: int, expected: int) -> bool:
    assert result == expected
    return True
