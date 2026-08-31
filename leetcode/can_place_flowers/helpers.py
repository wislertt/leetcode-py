def run_can_place_flowers(solution_class: type, flowerbed: list[int], n: int):
    implementation = solution_class()
    return implementation.can_place_flowers(flowerbed, n)


def assert_can_place_flowers(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
