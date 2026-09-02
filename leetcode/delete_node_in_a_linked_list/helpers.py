from leetcode_py import ListNode


def run_delete_node(solution_class: type, head_list: list[int], node_val: int):
    head = ListNode[int].from_list(head_list)
    assert head is not None
    target: ListNode[int] | None = head
    while target is not None and target.val != node_val:
        target = target.next
    assert target is not None
    implementation = solution_class()
    implementation.delete_node(target)
    return head.to_list()


def assert_delete_node(result: list[int], expected_list: list[int]) -> bool:
    assert result == expected_list
    return True
