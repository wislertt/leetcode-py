def run_image_smoother(solution_class: type, img: list[list[int]]):
    implementation = solution_class()
    return implementation.image_smoother(img)


def assert_image_smoother(result: list[list[int]], expected: list[list[int]]) -> bool:
    assert result == expected
    return True
