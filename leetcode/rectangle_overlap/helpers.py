def run_is_rectangle_overlap(solution_class: type, rec1: list[int], rec2: list[int]):
    implementation = solution_class()
    return implementation.is_rectangle_overlap(rec1, rec2)


def assert_is_rectangle_overlap(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
