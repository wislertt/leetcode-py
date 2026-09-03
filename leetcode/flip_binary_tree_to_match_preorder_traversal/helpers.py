from leetcode_py import TreeNode


def run_flip_match_voyage(solution_class: type, root_list: list[int | None], voyage: list[int]):
    root = TreeNode[int].from_list(root_list)
    implementation = solution_class()
    return implementation.flip_match_voyage(root, voyage)


def assert_flip_match_voyage(result: list[int], expected: list[int]) -> bool:
    # The answer may be returned in any order; [-1] means it is impossible
    if expected == [-1]:
        assert result == [-1]
        return True
    assert result != [-1]
    assert sorted(result) == expected
    return True
