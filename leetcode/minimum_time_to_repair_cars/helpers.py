def run_repair_cars(solution_class: type, ranks: list[int], cars: int):
    implementation = solution_class()
    return implementation.repair_cars(ranks, cars)


def assert_repair_cars(result: int, expected: int) -> bool:
    assert result == expected
    return True
