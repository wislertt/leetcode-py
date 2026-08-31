def run_interval_intersection(
    solution_class: type, first_list: list[list[int]], second_list: list[list[int]]
):
    implementation = solution_class()
    return implementation.interval_intersection(first_list, second_list)


def assert_interval_intersection(result: list[list[int]], expected: list[list[int]]) -> bool:
    assert result == expected
    return True
