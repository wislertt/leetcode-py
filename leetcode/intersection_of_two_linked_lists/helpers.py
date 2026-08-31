from leetcode_py import ListNode


def _build_intersection(
    list_a: list[int], list_b: list[int], skip_a: int, skip_b: int
) -> tuple[ListNode[int] | None, ListNode[int] | None, ListNode[int] | None]:
    head_a = ListNode[int].from_list(list_a)
    if skip_a >= len(list_a):
        head_b = ListNode[int].from_list(list_b)
        return head_a, head_b, None
    intersection: ListNode[int] | None = head_a
    for _ in range(skip_a):
        assert intersection is not None
        intersection = intersection.next
    assert intersection is not None
    if skip_b == 0:
        return head_a, intersection, intersection
    head_b = ListNode[int].from_list(list_b[:skip_b])
    tail: ListNode[int] | None = head_b
    while tail is not None and tail.next is not None:
        tail = tail.next
    assert tail is not None
    tail.next = intersection
    return head_a, head_b, intersection


def run_get_intersection_node(
    solution_class: type, list_a: list[int], list_b: list[int], skip_a: int, skip_b: int
):
    head_a, head_b, intersection = _build_intersection(list_a, list_b, skip_a, skip_b)
    implementation = solution_class()
    result = implementation.get_intersection_node(head_a, head_b)
    return result, intersection


def assert_get_intersection_node(
    result: ListNode[int] | None, expected: ListNode[int] | None
) -> bool:
    assert result is expected
    return True
