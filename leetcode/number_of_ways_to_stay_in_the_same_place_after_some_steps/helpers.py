def run_num_ways(solution_class: type, steps: int, arr_len: int):
    implementation = solution_class()
    return implementation.num_ways(steps, arr_len)


def assert_num_ways(result: int, expected: int) -> bool:
    assert result == expected
    return True
