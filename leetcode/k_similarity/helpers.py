def run_k_similarity(solution_class: type, s1: str, s2: str):
    implementation = solution_class()
    return implementation.k_similarity(s1, s2)


def assert_k_similarity(result: int, expected: int) -> bool:
    assert result == expected
    return True
