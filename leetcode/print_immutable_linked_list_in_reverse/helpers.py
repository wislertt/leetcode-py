from .solution import ImmutableListNode


def run_print_linked_list_in_reverse(solution_class: type, values: list[int]):
    ImmutableListNode.printed = []
    node: ImmutableListNode | None = None
    for value in reversed(values):
        node = ImmutableListNode(value, node)
    solution_class().print_linked_list_in_reverse(node)
    return ImmutableListNode.printed


def assert_print_linked_list_in_reverse(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
