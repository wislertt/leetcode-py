def run_number_of_alternating_groups(solution_class: type, colors: list[int], k: int):
    implementation = solution_class()
    return implementation.number_of_alternating_groups(colors, k)


def assert_number_of_alternating_groups(result: int, expected: int) -> bool:
    assert result == expected
    return True
