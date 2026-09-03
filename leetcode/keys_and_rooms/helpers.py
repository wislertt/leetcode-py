def run_can_visit_all_rooms(solution_class: type, rooms: list[list[int]]):
    implementation = solution_class()
    return implementation.can_visit_all_rooms(rooms)


def assert_can_visit_all_rooms(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
