def run_get_length_of_optimal_compression(solution_class: type, s: str, k: int):
    implementation = solution_class()
    return implementation.get_length_of_optimal_compression(s, k)


def assert_get_length_of_optimal_compression(result: int, expected: int) -> bool:
    assert result == expected
    return True
