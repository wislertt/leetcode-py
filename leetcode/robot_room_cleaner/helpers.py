from .solution import Robot


def run_clean_room(solution_class: type, room: list[list[int]], row: int, col: int):
    robot = Robot(room, row, col)
    solution_class().clean_room(robot)
    return len(robot.cleaned)


def assert_clean_room(result: int, expected: int) -> bool:
    assert result == expected
    return True
