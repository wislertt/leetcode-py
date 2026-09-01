def run_lucky_numbers(solution_class: type, matrix: list[list[int]]):
    implementation = solution_class()
    return implementation.lucky_numbers(matrix)


def assert_lucky_numbers(result: list[int], expected: list[int]) -> bool:
    assert sorted(result) == sorted(expected)
    return True
