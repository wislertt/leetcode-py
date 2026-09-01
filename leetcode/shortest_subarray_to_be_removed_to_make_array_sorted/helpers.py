def run_find_length_of_shortest_subarray(solution_class: type, arr: list[int]):
    implementation = solution_class()
    return implementation.find_length_of_shortest_subarray(arr)


def assert_find_length_of_shortest_subarray(result: int, expected: int) -> bool:
    assert result == expected
    return True
