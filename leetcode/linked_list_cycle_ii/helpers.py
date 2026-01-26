from leetcode_py import ListNode


def run_detect_cycle(solution_class: type, head_vals: list[int], pos: int):
    head = ListNode.from_list(head_vals)
    # Keep reference to tail to break cycle later
    tail = None
    if head is not None:
        tail = head
        while tail.next is not None:
            tail = tail.next
    # Create cycle if pos is valid
    if pos >= 0 and head is not None and tail is not None:
        # Find the node at position pos
        cycle_node = head
        for _ in range(pos):
            cycle_node = cycle_node.next
        # Create cycle
        tail.next = cycle_node
    implementation = solution_class()
    result = implementation.detect_cycle(head)
    # Break the cycle to avoid infinite loop when finding index
    if tail is not None:
        tail.next = None
    # Return the index of the cycle node, or -1 if no cycle
    if result is None:
        return -1
    # Find index of result node
    index = 0
    current = head
    while current is not None and current != result:
        current = current.next
        index += 1
    return index if current is not None else -1


def assert_detect_cycle(result: int, pos: int) -> bool:
    assert result == pos
    return True
