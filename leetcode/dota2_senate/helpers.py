def run_predict_party_victory(solution_class: type, senate: str):
    implementation = solution_class()
    return implementation.predict_party_victory(senate)


def assert_predict_party_victory(result: str, expected: str) -> bool:
    assert result == expected
    return True
