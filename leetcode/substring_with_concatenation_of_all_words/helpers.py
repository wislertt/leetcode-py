def run_find_substring(solution_class: type, s: str, words: list[str]):
    implementation = solution_class()
    return implementation.find_substring(s, words)


def assert_find_substring(result: list[int], expected: list[int]) -> bool:
    assert sorted(result) == sorted(expected)
    return True
