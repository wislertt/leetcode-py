def run_shortest_superstring(solution_class: type, words: list[str]):
    implementation = solution_class()
    return implementation.shortest_superstring(words)


def assert_shortest_superstring(result: str, expected: int) -> bool:
    # Any minimal-length superstring is accepted; every word is checked
    # against `result` in the test body since the helper only sees the length
    assert len(result) == expected
    return True
