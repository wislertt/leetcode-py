def run_maximum_beauty(solution_class: type, items: list[list[int]], queries: list[int]):
    implementation = solution_class()
    return implementation.maximum_beauty(items, queries)


def assert_maximum_beauty(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
