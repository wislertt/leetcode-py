def run_longest_palindrome_subseq(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.longest_palindrome_subseq(s)


def assert_longest_palindrome_subseq(result: int, expected: int) -> bool:
    assert result == expected
    return True
