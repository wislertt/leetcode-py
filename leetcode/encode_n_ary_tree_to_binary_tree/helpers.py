class NaryNode:
    def __init__(self, val: int = 0) -> None:
        self.val = val
        self.children: list[NaryNode] = []


def nary_from_list(vals: list[int | None]) -> NaryNode | None:
    if not vals:
        return None
    v0 = vals[0]
    assert v0 is not None
    root = NaryNode(v0)
    queue: list[NaryNode] = [root]
    i = 2
    while queue:
        node = queue.pop(0)
        while i < len(vals) and vals[i] is not None:
            v = vals[i]
            assert v is not None
            child = NaryNode(v)
            node.children.append(child)
            queue.append(child)
            i += 1
        i += 1
    return root


def nary_to_list(root: NaryNode | None) -> list[int | None]:
    if root is None:
        return []
    out: list[int | None] = [root.val, None]
    queue: list[NaryNode] = [root]
    while queue:
        node = queue.pop(0)
        for child in node.children:
            out.append(child.val)
            queue.append(child)
        if queue:
            out.append(None)
    while out and out[-1] is None:
        out.pop()
    return out


def run_encode_decode_n_ary(solution_class: type, root_list: list[int | None]):
    root = nary_from_list(root_list)
    codec = solution_class()
    binary = codec.encode(root)
    deserialized = codec.decode(binary)
    return nary_to_list(deserialized)


def assert_encode_decode_n_ary(result: list[int], expected_list: list[int | None]) -> bool:
    assert result == expected_list
    return True
