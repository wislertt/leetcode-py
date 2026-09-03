def run_num_similar_groups(solution_class: type, strs: list[str]):
    implementation = solution_class()
    return implementation.num_similar_groups(strs)


def assert_num_similar_groups(result: int, expected: int) -> bool:
    assert result == expected
    return True
