def run_construct_rectangle(solution_class: type, area: int):
    implementation = solution_class()
    return implementation.construct_rectangle(area)


def assert_construct_rectangle(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
