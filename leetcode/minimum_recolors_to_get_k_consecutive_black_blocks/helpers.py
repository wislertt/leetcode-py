def run_minimum_recolors(solution_class: type, blocks: str, k: int):
    implementation = solution_class()
    return implementation.minimum_recolors(blocks, k)


def assert_minimum_recolors(result: int, expected: int) -> bool:
    assert result == expected
    return True
