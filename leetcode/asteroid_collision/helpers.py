from typing import List


def run_asteroid_collision(solution_class: type, asteroids: List[int]):
    implementation = solution_class()
    return implementation.asteroid_collision(asteroids)


def assert_asteroid_collision(result: List[int], expected: List[int]) -> bool:
    assert result == expected
    return True
