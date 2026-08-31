def run_push_dominoes(solution_class: type, dominoes: str):
    implementation = solution_class()
    return implementation.push_dominoes(dominoes)


def assert_push_dominoes(result: str, expected: str) -> bool:
    assert result == expected
    return True
