def run_max_dist_to_closest(solution_class: type, seats: list[int]):
    implementation = solution_class()
    return implementation.max_dist_to_closest(seats)


def assert_max_dist_to_closest(result: int, expected: int) -> bool:
    assert result == expected
    return True
