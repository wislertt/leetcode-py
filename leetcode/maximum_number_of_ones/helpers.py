def run_maximum_number_of_ones(
    solution_class: type, width: int, height: int, side_length: int, max_ones: int
):
    implementation = solution_class()
    return implementation.maximum_number_of_ones(width, height, side_length, max_ones)


def assert_maximum_number_of_ones(result: int, expected: int) -> bool:
    assert result == expected
    return True
