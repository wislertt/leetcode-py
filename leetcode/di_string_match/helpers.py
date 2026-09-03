def run_di_string_match(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.di_string_match(s)


def assert_di_string_match(result: list[int], expected: list[int], s: str) -> bool:
    # Multiple valid permutations exist; validate the DI pattern, not exact equality
    assert len(expected) == len(s) + 1
    assert len(result) == len(s) + 1
    assert sorted(result) == list(range(len(s) + 1))
    assert all((result[i] < result[i + 1]) == (s[i] == "I") for i in range(len(s)))
    return True
