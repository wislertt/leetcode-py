def run_generate_possible_next_moves(solution_class: type, current_state: str):
    implementation = solution_class()
    return implementation.generate_possible_next_moves(current_state)


def assert_generate_possible_next_moves(result: list[str], expected: list[str]) -> bool:
    # Sort both result and expected for order-independent comparison
    result_sorted = sorted(result)
    expected_sorted = sorted(expected)
    assert result_sorted == expected_sorted
    return True
