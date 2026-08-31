def run_word_subsets(solution_class: type, words1: list[str], words2: list[str]):
    implementation = solution_class()
    return implementation.word_subsets(words1, words2)


def assert_word_subsets(result: list[str], expected: list[str]) -> bool:
    # Sort both result and expected for comparison since order doesn't matter
    assert sorted(result) == sorted(expected)
    return True
