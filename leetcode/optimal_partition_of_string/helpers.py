def run_partition_string(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.partition_string(s)


def assert_partition_string(result: int, expected: int) -> bool:
    assert result == expected
    return True
