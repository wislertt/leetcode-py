def run_partition_labels(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.partition_labels(s)


def assert_partition_labels(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
