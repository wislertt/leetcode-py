def run_len_longest_fib_subsequence(solution_class: type, arr: list[int]):
    implementation = solution_class()
    return implementation.len_longest_fib_subsequence(arr)


def assert_len_longest_fib_subsequence(result: int, expected: int) -> bool:
    assert result == expected
    return True
