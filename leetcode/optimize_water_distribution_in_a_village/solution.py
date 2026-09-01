class Solution:
    # Time: O((m + n) log(m + n)) where m = len(pipes), n = len(wells)
    # Space: O(n + m)
    def min_cost_to_supply_water(self, n: int, wells: list[int], pipes: list[list[int]]) -> int:
        # Virtual well node 0: connecting house i to it costs wells[i - 1].
        edges = [(w, 0, i + 1) for i, w in enumerate(wells)]
        edges += [(c, a, b) for a, b, c in pipes]
        edges.sort()

        parent = list(range(n + 1))

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        total = 0
        components = n + 1
        for cost, a, b in edges:
            ra, rb = find(a), find(b)
            if ra == rb:
                continue
            parent[ra] = rb
            total += cost
            components -= 1
            if components == 1:
                break
        return total
