def run_largest_overlap(solution_class: type, img1: list[list[int]], img2: list[list[int]]):
    implementation = solution_class()
    return implementation.largest_overlap(img1, img2)


def assert_largest_overlap(result: int, expected: int) -> bool:
    assert result == expected
    return True
