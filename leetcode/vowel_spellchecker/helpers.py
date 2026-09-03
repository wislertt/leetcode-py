def run_spellchecker(solution_class: type, wordlist: list[str], queries: list[str]):
    implementation = solution_class()
    return implementation.spellchecker(wordlist, queries)


def assert_spellchecker(result: list[str], expected: list[str]) -> bool:
    assert result == expected
    return True
