def run_reaching_points(solution_class: type, sx: int, sy: int, tx: int, ty: int):
    implementation = solution_class()
    return implementation.reaching_points(sx, sy, tx, ty)


def assert_reaching_points(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
