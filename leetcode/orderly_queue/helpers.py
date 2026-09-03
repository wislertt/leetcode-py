def run_orderly_queue(solution_class: type, s: str, k: int):
    implementation = solution_class()
    return implementation.orderly_queue(s, k)


def assert_orderly_queue(result: str, expected: str) -> bool:
    assert result == expected
    return True
