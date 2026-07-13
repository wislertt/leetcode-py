def run_num_rescue_boats(solution_class: type, people: list[int], limit: int):
    implementation = solution_class()
    return implementation.num_rescue_boats(people, limit)


def assert_num_rescue_boats(result: int, expected: int) -> bool:
    assert result == expected
    return True
