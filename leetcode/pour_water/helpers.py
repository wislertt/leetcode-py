def run_pour_water(solution_class: type, heights: list[int], volume: int, k: int):
    implementation = solution_class()
    return implementation.pour_water(heights, volume, k)


def assert_pour_water(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
