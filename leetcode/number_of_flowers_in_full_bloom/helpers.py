def run_full_bloom_flowers(solution_class: type, flowers: list[list[int]], people: list[int]):
    implementation = solution_class()
    return implementation.full_bloom_flowers(flowers, people)


def assert_full_bloom_flowers(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
