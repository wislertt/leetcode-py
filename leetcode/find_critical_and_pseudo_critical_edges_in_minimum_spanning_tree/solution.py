class Solution:
    # Time: O(m^2 * alpha(n)) where m = edges; runs Kruskal once + 2m times
    # Space: O(n + m)
    def find_critical_and_pseudo_critical_edges(
        self, n: int, edges: list[list[int]]
    ) -> list[list[int]]:
        m = len(edges)
        # Sort edges by (weight, original index) so tie-breaks are deterministic.
        order = sorted(range(m), key=lambda i: (edges[i][2], i))
        inf = 10**12

        def kruskal(skip: int = -1, force: int = -1) -> int:
            parent = list(range(n))

            def find(x: int) -> int:
                while parent[x] != x:
                    parent[x] = parent[parent[x]]
                    x = parent[x]
                return x

            weight = 0
            components = n

            if force != -1:
                u, v, w = edges[force]
                parent[find(u)] = find(v)
                weight += w
                components -= 1

            for i in order:
                if i in (skip, force):
                    continue
                u, v, w = edges[i]
                ru, rv = find(u), find(v)
                if ru != rv:
                    parent[ru] = rv
                    weight += w
                    components -= 1
                    if components == 1:
                        break

            return weight if components == 1 else inf

        base = kruskal()

        critical: list[int] = []
        pseudo: list[int] = []
        for i in range(m):
            # Excluding edge i: if the MST gets heavier (or impossible), it is critical.
            if kruskal(skip=i) > base:
                critical.append(i)
            # Forcing edge i into the MST: if weight is unchanged, it is in some MST.
            elif kruskal(force=i) == base:
                pseudo.append(i)

        return [critical, pseudo]
