def run_merge_triplets(solution_class: type, triplets: list[list[int]], target: list[int]):
    implementation = solution_class()
    return implementation.merge_triplets(triplets, target)


def assert_merge_triplets(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
