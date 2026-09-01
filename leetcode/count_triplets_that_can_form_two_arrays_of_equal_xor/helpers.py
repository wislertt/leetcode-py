def run_count_triplets(solution_class: type, arr: list[int]):
    implementation = solution_class()
    return implementation.count_triplets(arr)


def assert_count_triplets(result: int, expected: int) -> bool:
    assert result == expected
    return True
