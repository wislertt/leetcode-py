def run_sort_people(solution_class: type, names: list[str], heights: list[int]):
    implementation = solution_class()
    return implementation.sort_people(names, heights)


def assert_sort_people(result: list[str], expected: list[str]) -> bool:
    assert result == expected
    return True
