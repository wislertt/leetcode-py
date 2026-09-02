def run_find_rle_array(solution_class: type, encoded1: list[list[int]], encoded2: list[list[int]]):
    implementation = solution_class()
    return implementation.find_rle_array(encoded1, encoded2)


def assert_find_rle_array(result: list[list[int]], expected: list[list[int]]) -> bool:
    assert result == expected
    return True
