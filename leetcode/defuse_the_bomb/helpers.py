def run_decrypt(solution_class: type, code: list[int], k: int):
    implementation = solution_class()
    return implementation.decrypt(code, k)


def assert_decrypt(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
