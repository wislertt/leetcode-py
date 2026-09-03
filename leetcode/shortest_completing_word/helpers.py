def run_shortest_completing_word(solution_class: type, license_plate: str, words: list[str]):
    implementation = solution_class()
    return implementation.shortest_completing_word(license_plate, words)


def assert_shortest_completing_word(result: str, expected: str) -> bool:
    assert result == expected
    return True
