def run_car_fleet(solution_class: type, target: int, position: list[int], speed: list[int]):
    implementation = solution_class()
    return implementation.car_fleet(target, position, speed)


def assert_car_fleet(result: int, expected: int) -> bool:
    assert result == expected
    return True
