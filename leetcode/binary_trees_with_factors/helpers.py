def run_num_factored_binary_trees(solution_class: type, arr: list[int]):
    implementation = solution_class()
    return implementation.num_factored_binary_trees(arr)


def assert_num_factored_binary_trees(result: int, expected: int) -> bool:
    assert result == expected
    return True
