def run_flip_and_invert_image(solution_class: type, image: list[list[int]]):
    implementation = solution_class()
    return implementation.flip_and_invert_image(image)


def assert_flip_and_invert_image(result: list[list[int]], expected: list[list[int]]) -> bool:
    assert result == expected
    return True
