def run_num_trees(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.num_trees(n)


def assert_num_trees(result: int, expected: int) -> bool:
    assert result == expected
    return True
