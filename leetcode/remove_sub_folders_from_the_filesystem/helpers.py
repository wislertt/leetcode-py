def run_remove_subfolders(solution_class: type, folder: list[str]):
    implementation = solution_class()
    return implementation.remove_subfolders(folder)


def assert_remove_subfolders(result: list[str], expected: list[str]) -> bool:
    assert sorted(result) == sorted(expected)
    return True
