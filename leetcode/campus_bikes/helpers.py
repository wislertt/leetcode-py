def run_assign_bikes(solution_class: type, workers: list[list[int]], bikes: list[list[int]]):
    implementation = solution_class()
    return implementation.assign_bikes(workers, bikes)


def assert_assign_bikes(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
