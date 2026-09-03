def run_contain_virus(solution_class: type, is_infected: list[list[int]]):
    import copy

    grid_copy = copy.deepcopy(is_infected)
    implementation = solution_class()
    return implementation.contain_virus(grid_copy)


def assert_contain_virus(result: int, expected: int) -> bool:
    assert result == expected
    return True
