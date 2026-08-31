def run_num_k_len_substr_no_repeats(solution_class: type, s: str, k: int):
    implementation = solution_class()
    return implementation.num_k_len_substr_no_repeats(s, k)


def assert_num_k_len_substr_no_repeats(result: int, expected: int) -> bool:
    assert result == expected
    return True
