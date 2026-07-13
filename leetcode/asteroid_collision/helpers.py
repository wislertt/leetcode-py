def run_asteroid_collision(solution_class: type, asteroids: list[int]):
    implementation = solution_class()
    return implementation.asteroid_collision(asteroids)


def assert_asteroid_collision(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
