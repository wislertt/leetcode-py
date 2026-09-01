def run_longest_obstacle_course(solution_class: type, obstacles: list[int]):
    implementation = solution_class()
    return implementation.longest_obstacle_course(obstacles)


def assert_longest_obstacle_course(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
