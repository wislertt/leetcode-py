def run_valid_square(
    solution_class: type, p1: list[int], p2: list[int], p3: list[int], p4: list[int]
):
    implementation = solution_class()
    return implementation.valid_square(p1, p2, p3, p4)


def assert_valid_square(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
