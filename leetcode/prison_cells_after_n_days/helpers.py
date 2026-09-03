def run_prison_after_n_days(solution_class: type, cells: list[int], n: int):
    implementation = solution_class()
    return implementation.prison_after_n_days(cells, n)


def assert_prison_after_n_days(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
