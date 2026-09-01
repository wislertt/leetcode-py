def run_probability_of_heads(solution_class: type, prob: list[float], target: int):
    implementation = solution_class()
    return implementation.probability_of_heads(prob, target)


def assert_probability_of_heads(result: float, expected: float) -> bool:
    # Expectations are exact values computed with fractions.Fraction; the
    # float DP stays far inside this tolerance (statement allows 10^-5)
    assert abs(result - expected) < 1e-9
    return True
