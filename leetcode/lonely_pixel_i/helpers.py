def run_find_lonely_pixel(solution_class: type, picture: list[list[str]]):
    implementation = solution_class()
    return implementation.find_lonely_pixel(picture)


def assert_find_lonely_pixel(result: int, expected: int) -> bool:
    assert result == expected
    return True
