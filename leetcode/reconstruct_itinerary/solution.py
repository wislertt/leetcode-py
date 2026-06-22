class Solution:
    # Time: O(E log E)
    # Space: O(E)
    def find_itinerary(self, tickets: list[list[str]]) -> list[str]:
        graph: dict[str, list[str]] = {}
        for src, dst in tickets:
            graph.setdefault(src, []).append(dst)
        for src in graph:
            graph[src].sort(reverse=True)

        itinerary: list[str] = []

        def dfs(airport: str) -> None:
            destinations = graph.get(airport)
            while destinations:
                dfs(destinations.pop())
            itinerary.append(airport)

        dfs("JFK")
        itinerary.reverse()
        return itinerary
