def run_max_chunks_to_sorted(solution_class: type, arr: list[int]):
    implementation = solution_class()
    return implementation.max_chunks_to_sorted(arr)


def assert_max_chunks_to_sorted(result: int, expected: int) -> bool:
    assert result == expected
    return True
