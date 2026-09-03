def run_preimage_size_fzf(solution_class: type, k: int):
    implementation = solution_class()
    return implementation.preimage_size_fzf(k)


def assert_preimage_size_fzf(result: int, expected: int) -> bool:
    assert result == expected, f"Expected {expected}, got {result}"
    return True
