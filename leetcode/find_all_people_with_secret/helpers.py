def run_find_all_people(solution_class: type, n: int, meetings: list[list[int]], first_person: int):
    implementation = solution_class()
    return implementation.find_all_people(n, meetings, first_person)


def assert_find_all_people(result: list[int], expected: list[int]) -> bool:
    # The answer may be returned in any order
    assert sorted(result) == sorted(expected)
    return True
