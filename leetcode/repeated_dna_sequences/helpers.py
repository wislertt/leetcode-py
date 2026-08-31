def run_repeated_dna_sequences(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.repeated_dna_sequences(s)


def assert_repeated_dna_sequences(result: list[str], expected: list[str]) -> bool:
    assert sorted(result) == sorted(expected)
    return True
