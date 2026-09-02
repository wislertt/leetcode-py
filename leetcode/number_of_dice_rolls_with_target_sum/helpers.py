def run_num_rolls_to_target(solution_class: type, n: int, k: int, target: int):
    implementation = solution_class()
    return implementation.num_rolls_to_target(n, k, target)


def assert_num_rolls_to_target(result: int, expected: int) -> bool:
    assert result == expected
    return True
