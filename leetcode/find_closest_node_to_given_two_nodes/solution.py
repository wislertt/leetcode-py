class Solution:
    # Time: O(n)
    # Space: O(n)
    def closest_meeting_node(self, edges: list[int], node1: int, node2: int) -> int:
        def distances(start: int) -> list[int]:
            dist = [-1] * len(edges)
            node = start
            step = 0
            while node != -1 and dist[node] == -1:
                dist[node] = step
                node = edges[node]
                step += 1
            return dist

        dist1 = distances(node1)
        dist2 = distances(node2)
        best_node = -1
        best_max = -1
        for i in range(len(edges)):
            if dist1[i] == -1 or dist2[i] == -1:
                continue
            curr_max = max(dist1[i], dist2[i])
            if best_node == -1 or curr_max < best_max:
                best_node = i
                best_max = curr_max
        return best_node
