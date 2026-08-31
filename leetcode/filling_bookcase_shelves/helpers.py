def run_min_height_shelves(solution_class: type, books: list[list[int]], shelf_width: int):
    implementation = solution_class()
    return implementation.min_height_shelves(books, shelf_width)


def assert_min_height_shelves(result: int, expected: int) -> bool:
    assert result == expected
    return True
