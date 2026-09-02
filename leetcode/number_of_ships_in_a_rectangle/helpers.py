from .solution import Point, Sea


def run_count_ships(
    solution_class: type, ships: list[list[int]], top_right: list[int], bottom_left: list[int]
):
    sea = Sea(ships)
    top = Point(top_right[0], top_right[1])
    bottom = Point(bottom_left[0], bottom_left[1])
    return solution_class().count_ships(sea, top, bottom)


def assert_count_ships(result: int, expected: int) -> bool:
    assert result == expected
    return True
