from collections import Counter, defaultdict


class Solution:
    # Time: O(n^3) per user in the worst case, n = visits per user
    # Space: O(n^3) for the distinct triplets
    def most_visited_pattern(
        self, username: list[str], timestamp: list[int], website: list[str]
    ) -> list[str]:
        visits: dict[str, list[tuple[int, str]]] = defaultdict(list)
        for user, ts, site in zip(username, timestamp, website, strict=True):
            visits[user].append((ts, site))

        scores: Counter[tuple[str, str, str]] = Counter()
        for entries in visits.values():
            sites = [site for _, site in sorted(entries)]
            count = len(sites)
            patterns = {
                (sites[i], sites[j], sites[k])
                for i in range(count - 2)
                for j in range(i + 1, count - 1)
                for k in range(j + 1, count)
            }
            scores.update(patterns)

        best = min(scores.items(), key=lambda item: (-item[1], item[0]))[0]
        return list(best)
