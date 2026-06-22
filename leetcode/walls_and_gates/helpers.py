def run_walls_and_gates(solution_class: type, rooms: list[list[int]]):
    import copy

    rooms_copy = copy.deepcopy(rooms)
    implementation = solution_class()
    implementation.walls_and_gates(rooms_copy)
    return rooms_copy


def assert_walls_and_gates(result: list[list[int]], expected: list[list[int]]) -> bool:
    assert result == expected
    return True
