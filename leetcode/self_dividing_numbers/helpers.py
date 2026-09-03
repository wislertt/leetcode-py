def run_self_dividing_numbers(solution_class: type, left: int, right: int):
    implementation = solution_class()
    return implementation.self_dividing_numbers(left, right)


def assert_self_dividing_numbers(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
