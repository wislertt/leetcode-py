def run_min_moves_to_seat(solution_class: type, seats: list[int], students: list[int]):
    implementation = solution_class()
    return implementation.min_moves_to_seat(seats, students)


def assert_min_moves_to_seat(result: int, expected: int) -> bool:
    assert result == expected
    return True
