def run_min_stickers(solution_class: type, stickers: list[str], target: str):
    implementation = solution_class()
    return implementation.min_stickers(stickers, target)


def assert_min_stickers(result: int, expected: int) -> bool:
    assert result == expected
    return True
