class UndergroundSystem:
    # Time: check_in O(1), check_out O(1), get_average_time O(1)
    # Space: O(P + R) for P passengers in transit and R distinct routes
    def __init__(self) -> None:
        self.checked_in: dict[int, tuple[str, int]] = {}
        self.trips: dict[tuple[str, str], tuple[int, int]] = {}

    def check_in(self, id: int, station_name: str, t: int) -> None:
        self.checked_in[id] = (station_name, t)

    def check_out(self, id: int, station_name: str, t: int) -> None:
        start_station, start_t = self.checked_in.pop(id)
        route = (start_station, station_name)
        total, count = self.trips.get(route, (0, 0))
        self.trips[route] = (total + t - start_t, count + 1)

    def get_average_time(self, start_station: str, end_station: str) -> float:
        total, count = self.trips[(start_station, end_station)]
        return total / count
