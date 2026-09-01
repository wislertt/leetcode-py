def run_traffic_light(solution_class: type, operations: list[str], inputs: list[list[int]]):
    light = None
    events: list[str] = []

    def turn_green(road_id: int) -> None:
        events.append(f"Traffic Light On Road {'AB'[road_id - 1]} Is Green")

    def cross_car(car_id: int, road_id: int, direction: int) -> None:
        road = "AB"[road_id - 1]
        events.append(f"Car {car_id} Has Passed Road {road} In Direction {direction}")

    for i, op in enumerate(operations):
        if op == "TrafficLight":
            light = solution_class()
        elif op == "car_arrived" and light is not None:
            car_id, road_id, direction = inputs[i]

            def turn(road_id: int = road_id) -> None:
                turn_green(road_id)

            def cross(
                car_id: int = car_id, road_id: int = road_id, direction: int = direction
            ) -> None:
                cross_car(car_id, road_id, direction)

            light.car_arrived(car_id, road_id, direction, turn, cross)
    return events, light


def assert_traffic_light(result: list[str], expected: list[str]) -> bool:
    assert result == expected
    return True
