def run_min_deletion_size(solution_class: type, strs: list[str]):
    implementation = solution_class()
    return implementation.min_deletion_size(strs)


def assert_min_deletion_size(result: int, expected: int) -> bool:
    assert result == expected
    return True
