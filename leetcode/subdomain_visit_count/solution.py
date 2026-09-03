from collections import Counter


class Solution:
    # Time: O(n * m) where n is the number of domains and m is the label count
    # Space: O(n * m) for the counter of subdomains
    def subdomain_visits(self, cpdomains: list[str]) -> list[str]:
        counts: Counter[str] = Counter()
        for entry in cpdomains:
            rep_str, domain = entry.split(" ")
            labels = domain.split(".")
            for i in range(len(labels)):
                counts[".".join(labels[i:])] += int(rep_str)
        return [f"{rep} {domain}" for domain, rep in counts.items()]
