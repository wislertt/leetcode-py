from collections import deque


class Solution:
    # Time: O(8^2 * n) where n = len(bank), each gene expands 8*4 neighbors
    # Space: O(n)
    def min_mutation(self, start_gene: str, end_gene: str, bank: list[str]) -> int:
        valid = set(bank)
        if start_gene == end_gene:
            return 0
        if end_gene not in valid:
            return -1
        queue: deque[tuple[str, int]] = deque([(start_gene, 0)])
        visited = {start_gene}
        while queue:
            gene, steps = queue.popleft()
            if gene == end_gene:
                return steps
            for i in range(len(gene)):
                for c in "ACGT":
                    if c == gene[i]:
                        continue
                    nxt = gene[:i] + c + gene[i + 1 :]
                    if nxt in valid and nxt not in visited:
                        visited.add(nxt)
                        queue.append((nxt, steps + 1))
        return -1
