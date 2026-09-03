def run_fair_candy_swap(solution_class: type, alice_sizes: list[int], bob_sizes: list[int]):
    implementation = solution_class()
    return implementation.fair_candy_swap(alice_sizes, bob_sizes)


def assert_fair_candy_swap(result: list[int], expected: list[int]) -> bool:
    # Multiple valid swaps may exist; verify the exchange equalizes the
    # totals rather than matching one exact answer
    assert len(result) == 2
    assert result[0] - result[1] == expected[0] - expected[1]
    return True
