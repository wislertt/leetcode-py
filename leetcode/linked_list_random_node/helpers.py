from typing import Any

from leetcode_py import ListNode


def run_linked_list_random_node(
    solution_class: type, operations: list[str], inputs: list[list[int]]
):
    obj: Any = None
    results: list[int | None] = []
    for i, op in enumerate(operations):
        if op == "Solution":
            head = ListNode[int].from_list(inputs[i])
            obj = solution_class(head)
            results.append(None)
        elif op == "get_random" and obj is not None:
            results.append(obj.get_random())
    return results


def assert_linked_list_random_node(result: list[int | None], expected: list[int]) -> bool:
    # getRandom() is random; any node value is a valid answer, so verify
    # every returned value belongs to the list instead of exact equality
    assert len(result) >= 2
    assert result[0] is None
    assert all(value is None or value in expected for value in result)
    assert any(value is not None for value in result)
    return True
