def run_find_black_pixel(solution_class: type, picture: list[list[str]], target: int):
    implementation = solution_class()
    return implementation.find_black_pixel(picture, target)


def assert_find_black_pixel(result: int, expected: int) -> bool:
    assert result == expected
    return True
