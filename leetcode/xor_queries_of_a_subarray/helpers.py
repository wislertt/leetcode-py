def run_xor_queries(solution_class: type, arr: list[int], queries: list[list[int]]):
    implementation = solution_class()
    return implementation.xor_queries(arr, queries)


def assert_xor_queries(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
