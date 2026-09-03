def run_find_restaurant(solution_class: type, list1: list[str], list2: list[str]):
    implementation = solution_class()
    return implementation.find_restaurant(list1, list2)


def assert_find_restaurant(result: list[str], expected: list[str]) -> bool:
    assert sorted(result) == sorted(expected)
    return True
