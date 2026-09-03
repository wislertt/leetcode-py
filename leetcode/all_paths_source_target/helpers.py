from itertools import pairwise


def count_paths_source_target(graph: list[list[int]]) -> int:
    n = len(graph)
    memo: dict[int, int] = {}

    def dfs(node: int) -> int:
        if node == n - 1:
            return 1
        if node not in memo:
            memo[node] = sum(dfs(nxt) for nxt in graph[node])
        return memo[node]

    return dfs(0)


def assert_all_paths_source_target_count(
    result: list[list[int]], graph: list[list[int]], expected_count: int
) -> bool:
    n = len(graph)
    unique = {tuple(path) for path in result}
    assert len(unique) == len(result)
    for path in result:
        assert path[0] == 0
        assert path[-1] == n - 1
        for a, b in pairwise(path):
            assert b in graph[a]
    assert len(unique) == count_paths_source_target(graph)
    assert len(result) == expected_count
    return True


def run_all_paths_source_target(solution_class: type, graph: list[list[int]]):
    implementation = solution_class()
    return implementation.all_paths_source_target(graph)


def assert_all_paths_source_target(result: list[list[int]], expected: list[list[int]]) -> bool:
    # Sort both result and expected for order-independent comparison
    result_sorted = sorted(result)
    expected_sorted = sorted(expected)
    assert result_sorted == expected_sorted
    return True
