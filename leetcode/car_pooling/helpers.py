def run_car_pooling(solution_class: type, trips: list[list[int]], capacity: int):
    implementation = solution_class()
    return implementation.car_pooling(trips, capacity)


def assert_car_pooling(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
