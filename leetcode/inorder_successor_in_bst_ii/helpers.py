class TreeNodeP:
    def __init__(self, val: int = 0) -> None:
        self.val = val
        self.left: TreeNodeP | None = None
        self.right: TreeNodeP | None = None
        self.parent: TreeNodeP | None = None


def build_parent_tree(vals: list[int | None]) -> TreeNodeP | None:
    if not vals:
        return None
    v0 = vals[0]
    assert v0 is not None
    root = TreeNodeP(v0)
    queue: list[TreeNodeP] = [root]
    i = 1
    while queue and i < len(vals):
        node = queue.pop(0)
        if i < len(vals):
            v = vals[i]
            i += 1
            if v is not None:
                child = TreeNodeP(v)
                child.parent = node
                node.left = child
                queue.append(child)
        if i < len(vals):
            v = vals[i]
            i += 1
            if v is not None:
                child = TreeNodeP(v)
                child.parent = node
                node.right = child
                queue.append(child)
    return root


def find_node(root: TreeNodeP | None, val: int) -> TreeNodeP | None:
    if root is None:
        return None
    if root.val == val:
        return root
    return find_node(root.left, val) or find_node(root.right, val)


def run_inorder_successor(solution_class: type, root_list: list[int | None], node_val: int):
    root = build_parent_tree(root_list)
    node = find_node(root, node_val)
    implementation = solution_class()
    return implementation.inorder_successor(node)


def assert_inorder_successor(result: TreeNodeP | None, expected_val: int | None) -> bool:
    if expected_val is None:
        assert result is None
    else:
        assert result is not None
        assert result.val == expected_val
    return True
