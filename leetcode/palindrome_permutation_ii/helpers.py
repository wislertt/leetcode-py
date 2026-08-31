def assert_generate_palindromes_count(result: list[str], expected: int) -> bool:
    assert len(result) == expected
    return True


def run_generate_palindromes(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.generate_palindromes(s)


def assert_generate_palindromes(result: list[str], expected: list[str]) -> bool:
    # Sort both result and expected for order-independent comparison
    result_sorted = sorted(result)
    expected_sorted = sorted(expected)
    assert result_sorted == expected_sorted
    return True
