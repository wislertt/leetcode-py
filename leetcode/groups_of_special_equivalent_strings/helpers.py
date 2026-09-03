def run_num_special_equivalent_groups(solution_class: type, words: list[str]):
    implementation = solution_class()
    return implementation.num_special_equivalent_groups(words)


def assert_num_special_equivalent_groups(result: int, expected: int) -> bool:
    assert result == expected
    return True
