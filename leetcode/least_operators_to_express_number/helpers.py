def run_least_ops_express_target(solution_class: type, x: int, target: int):
    implementation = solution_class()
    return implementation.least_ops_express_target(x, target)


def assert_least_ops_express_target(result: int, expected: int) -> bool:
    assert result == expected
    return True
