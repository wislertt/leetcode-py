def run_triplet_count(solution_class: type, a: list[int], b: list[int], c: list[int]):
    implementation = solution_class()
    return implementation.triplet_count(a, b, c)


def assert_triplet_count(result: int, expected: int) -> bool:
    assert result == expected
    return True
