class Solution:
    # Time: O(n^2 * L + n * alpha(n)) for n words of length L
    # Space: O(n)
    def num_similar_groups(self, strs: list[str]) -> int:
        parent = list(range(len(strs)))
        rank = [0] * len(strs)

        def find(i: int) -> int:
            while parent[i] != i:
                parent[i] = parent[parent[i]]
                i = parent[i]
            return i

        def union(i: int, j: int) -> bool:
            root_i, root_j = find(i), find(j)
            if root_i == root_j:
                return False
            if rank[root_i] < rank[root_j]:
                root_i, root_j = root_j, root_i
            parent[root_j] = root_i
            if rank[root_i] == rank[root_j]:
                rank[root_i] += 1
            return True

        def similar(a: str, b: str) -> bool:
            first = second = -1
            for i, (x, y) in enumerate(zip(a, b, strict=True)):
                if x != y:
                    if second >= 0:
                        return False
                    if first < 0:
                        first = i
                    else:
                        second = i
            return first < 0 or (second >= 0 and a[first] == b[second])

        groups = len(strs)
        for i in range(len(strs)):
            for j in range(i + 1, len(strs)):
                if similar(strs[i], strs[j]) and union(i, j):
                    groups -= 1
        return groups
