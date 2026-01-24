def run_partition(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.partition(s)


def assert_partition(result: list[list[str]], expected: list[list[str]]) -> bool:
    # Sort inner lists and outer list for comparison
    # Note: Inner lists are partitions (lists of strings), order of partitions doesn't matter
    # Order of strings within a partition DOES matter (it must reconstruct s)
    # But wait, the problem says "partition s", so order of substrings must match the order in s.
    # So we only need to sort the outer list of partitions.
    result_sorted = sorted(result)
    expected_sorted = sorted(expected)
    assert result_sorted == expected_sorted
    return True
