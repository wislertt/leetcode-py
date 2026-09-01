class Solution:
    # Time: O(nodes)
    # Space: O(nodes)
    def delete_tree_nodes(self, nodes: int, parent: list[int], value: list[int]) -> int:
        children: list[list[int]] = [[] for _ in range(nodes)]
        for i in range(1, nodes):
            children[parent[i]].append(i)

        # Iterative post-order keeps deep chains within the recursion limit.
        subtree_sums = [0] * nodes
        subtree_counts = [0] * nodes
        stack: list[tuple[int, bool]] = [(0, False)]
        while stack:
            node, processed = stack.pop()
            if processed:
                total, count = value[node], 1
                for child in children[node]:
                    total += subtree_sums[child]
                    count += subtree_counts[child]
                if total == 0:
                    count = 0
                subtree_sums[node], subtree_counts[node] = total, count
            else:
                stack.append((node, True))
                stack.extend((child, False) for child in children[node])
        return subtree_counts[0]
