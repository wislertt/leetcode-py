def run_deck_revealed_increasing(solution_class: type, deck: list[int]):
    implementation = solution_class()
    return implementation.deck_revealed_increasing(deck)


def assert_deck_revealed_increasing(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
