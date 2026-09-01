def run_min_cost_to_supply_water(
    solution_class: type, n: int, wells: list[int], pipes: list[list[int]]
):
    implementation = solution_class()
    return implementation.min_cost_to_supply_water(n, wells, pipes)


def assert_min_cost_to_supply_water(result: int, expected: int) -> bool:
    assert result == expected
    return True
