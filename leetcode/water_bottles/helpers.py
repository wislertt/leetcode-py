def run_num_water_bottles(solution_class: type, num_bottles: int, num_exchange: int):
    implementation = solution_class()
    return implementation.num_water_bottles(num_bottles, num_exchange)


def assert_num_water_bottles(result: int, expected: int) -> bool:
    assert result == expected
    return True
