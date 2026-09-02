def run_compute_area(
    solution_class: type,
    ax1: int,
    ay1: int,
    ax2: int,
    ay2: int,
    bx1: int,
    by1: int,
    bx2: int,
    by2: int,
):
    implementation = solution_class()
    return implementation.compute_area(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)


def assert_compute_area(result: int, expected: int) -> bool:
    assert result == expected
    return True
