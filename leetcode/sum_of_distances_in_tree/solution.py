class Solution:
    # Time: O(n) build + two O(n) traversals
    # Space: O(n) adjacency, subtree counts and output
    def sum_of_distances_in_tree(self, n: int, edges: list[list[int]]) -> list[int]:
        graph: list[list[int]] = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        subtree_size = [1] * n
        answer = [0] * n

        # Post-order from root 0: count descendants and sum depths below each node.
        stack: list[tuple[int, int, bool]] = [(0, -1, False)]
        while stack:
            node, parent, processed = stack.pop()
            if not processed:
                stack.append((node, parent, True))
                for child in graph[node]:
                    if child != parent:
                        stack.append((child, node, False))
            else:
                for child in graph[node]:
                    if child != parent:
                        subtree_size[node] += subtree_size[child]
                        answer[node] += answer[child] + subtree_size[child]

        # Pre-order reroot: moving the root from parent to child shifts the sum by
        # size(child) closer minus (n - size(child)) farther.
        reroot_stack: list[tuple[int, int]] = [(0, -1)]
        while reroot_stack:
            node, parent = reroot_stack.pop()
            for child in graph[node]:
                if child != parent:
                    answer[child] = answer[node] + n - 2 * subtree_size[child]
                    reroot_stack.append((child, node))

        return answer
