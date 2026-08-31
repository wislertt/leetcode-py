def run_verify_preorder(solution_class: type, preorder: list[int]):
    implementation = solution_class()
    return implementation.verify_preorder(preorder)


def assert_verify_preorder(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
