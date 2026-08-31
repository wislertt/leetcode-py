def run_uncommon_from_sentences(solution_class: type, s1: str, s2: str):
    implementation = solution_class()
    return implementation.uncommon_from_sentences(s1, s2)


def assert_uncommon_from_sentences(result: list[str], expected: list[str]) -> bool:
    # Sort both result and expected for comparison since order doesn't matter
    assert sorted(result) == sorted(expected)
    return True
