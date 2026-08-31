def run_robot_sim(solution_class: type, commands: list[int], obstacles: list[list[int]]):
    implementation = solution_class()
    return implementation.robot_sim(commands, obstacles)


def assert_robot_sim(result: int, expected: int) -> bool:
    assert result == expected
    return True
