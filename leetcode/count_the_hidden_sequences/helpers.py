def run_number_of_arrays(solution_class: type, differences: list[int], lower: int, upper: int):
    implementation = solution_class()
    return implementation.number_of_arrays(differences, lower, upper)


def assert_number_of_arrays(result: int, expected: int) -> bool:
    assert result == expected
    return True
