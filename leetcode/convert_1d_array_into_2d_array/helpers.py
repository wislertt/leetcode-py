def run_construct_2d_array(solution_class: type, original: list[int], m: int, n: int):
    implementation = solution_class()
    return implementation.construct_2d_array(original, m, n)


def assert_construct_2d_array(result: list[list[int]], expected: list[list[int]]) -> bool:
    assert result == expected
    return True
