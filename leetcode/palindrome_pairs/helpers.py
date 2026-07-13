def run_palindrome_pairs(solution_class: type, words: list[str]):
    implementation = solution_class()
    return implementation.palindrome_pairs(words)


def assert_palindrome_pairs(result: list[list[int]], expected: list[list[int]]) -> bool:
    # Pair order does not matter; sort outer list for comparison
    assert sorted(result) == sorted(expected)
    return True
