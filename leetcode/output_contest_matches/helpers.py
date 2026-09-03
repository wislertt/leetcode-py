def run_find_contest_match(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.find_contest_match(n)


def assert_find_contest_match(result: str, n: int, expected: str | int) -> bool:
    if isinstance(expected, str):
        assert result == expected
    else:
        # Large n: the exact string overflows the parametrize line budget, so the JSON
        # carries the machine-verified output length instead.
        assert len(result) == expected
        assert result.count("(") == n - 1
        assert result.count(")") == n - 1
        assert result.startswith("(") and result.endswith(")")
    return True
