from collections.abc import Callable
from threading import Lock


class TrafficLight:
    # Time: O(1) per car
    # Space: O(1)

    def __init__(self) -> None:
        self.lock = Lock()
        self.road = 1

    def car_arrived(
        self,
        car_id: int,
        road_id: int,
        direction: int,
        turn_green: Callable[[], None],
        cross_car: Callable[[], None],
    ) -> None:
        with self.lock:
            if self.road != road_id:
                turn_green()
                self.road = road_id
            cross_car()
