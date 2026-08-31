def run_linked_list_ops(solution_class: type, operations: list[str], inputs: list[list[int]]):
    linked_list = None
    results: list[int | None] = []
    for i, op in enumerate(operations):
        if op == "MyLinkedList":
            linked_list = solution_class()
            results.append(None)
        elif op == "get" and linked_list is not None:
            results.append(linked_list.get(inputs[i][0]))
        elif op == "add_at_head" and linked_list is not None:
            linked_list.add_at_head(inputs[i][0])
            results.append(None)
        elif op == "add_at_tail" and linked_list is not None:
            linked_list.add_at_tail(inputs[i][0])
            results.append(None)
        elif op == "add_at_index" and linked_list is not None:
            linked_list.add_at_index(inputs[i][0], inputs[i][1])
            results.append(None)
        elif op == "delete_at_index" and linked_list is not None:
            linked_list.delete_at_index(inputs[i][0])
            results.append(None)
    return results, linked_list


def assert_linked_list_ops(result: list[int | None], expected: list[int | None]) -> bool:
    assert result == expected
    return True
