def run_num_tile_possibilities(solution_class: type, tiles: str):
    implementation = solution_class()
    return implementation.num_tile_possibilities(tiles)


def assert_num_tile_possibilities(result: int, expected: int) -> bool:
    assert result == expected
    return True
