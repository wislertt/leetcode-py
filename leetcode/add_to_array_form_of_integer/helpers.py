def run_add_to_array_form(solution_class: type, num: list[int], k: int):
    implementation = solution_class()
    return implementation.add_to_array_form(num, k)


def assert_add_to_array_form(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
