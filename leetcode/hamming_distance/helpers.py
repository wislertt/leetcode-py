def run_hamming_distance(solution_class: type, x: int, y: int):
    implementation = solution_class()
    return implementation.hamming_distance(x, y)


def assert_hamming_distance(result: int, expected: int) -> bool:
    assert result == expected
    return True
