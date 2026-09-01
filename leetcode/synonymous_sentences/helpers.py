def run_generate_sentences(solution_class: type, synonyms: list[list[str]], text: str):
    implementation = solution_class()
    return implementation.generate_sentences(synonyms, text)


def assert_generate_sentences(result: list[str], expected: list[str]) -> bool:
    assert result == expected
    return True
