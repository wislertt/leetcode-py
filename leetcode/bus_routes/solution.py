from collections import defaultdict, deque


class Solution:
    # BFS over buses, not stops. Each bus is one hop. Map stop -> buses that
    # serve it. From source, enqueue all buses containing it; ride a bus to
    # reach every stop on it, transferring to unvisited buses at those stops.
    # Time: O(sum of routes length)
    # Space: O(sum of routes length)
    def num_buses_to_destination(self, routes: list[list[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        stop_to_buses: dict[int, list[int]] = defaultdict(list)
        for bus, stops in enumerate(routes):
            for stop in stops:
                stop_to_buses[stop].append(bus)

        # source or target unreachable
        if source not in stop_to_buses or target not in stop_to_buses:
            return -1

        used_buses: set[int] = set()
        queue: deque[tuple[int, int]] = deque()
        for bus in stop_to_buses[source]:
            queue.append((bus, 1))
            used_buses.add(bus)

        while queue:
            bus, buses_taken = queue.popleft()
            for stop in routes[bus]:
                if stop == target:
                    return buses_taken
                for next_bus in stop_to_buses[stop]:
                    if next_bus not in used_buses:
                        used_buses.add(next_bus)
                        queue.append((next_bus, buses_taken + 1))

        return -1
