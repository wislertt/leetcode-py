def run_min_remove_to_make_valid(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.min_remove_to_make_valid(s)


def assert_min_remove_to_make_valid(result: str, expected: str) -> bool:
    balance = 0
    for char in result:
        if char == "(":
            balance += 1
        elif char == ")":
            balance -= 1
            assert balance >= 0
    assert balance == 0
    assert [c for c in result if c.isalpha()] == [c for c in expected if c.isalpha()]
    assert len(result) == len(expected)
    return True
