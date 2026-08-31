def run_regions_by_slashes(solution_class: type, grid: list[str]):
    implementation = solution_class()
    return implementation.regions_by_slashes(grid)


def assert_regions_by_slashes(result: int, expected: int) -> bool:
    assert result == expected
    return True
