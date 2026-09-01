def run_number_of_good_paths(solution_class: type, vals: list[int], edges: list[list[int]]):
    implementation = solution_class()
    return implementation.number_of_good_paths(vals, edges)


def assert_number_of_good_paths(result: int, expected: int) -> bool:
    assert result == expected
    return True
