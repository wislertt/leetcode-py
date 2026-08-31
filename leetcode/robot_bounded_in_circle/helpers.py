def run_is_robot_bounded(solution_class: type, instructions: str):
    implementation = solution_class()
    return implementation.is_robot_bounded(instructions)


def assert_is_robot_bounded(result: bool, expected: bool) -> bool:
    assert result is expected
    return True
