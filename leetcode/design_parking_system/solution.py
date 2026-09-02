class ParkingSystem:
    # Time: O(1) per call
    # Space: O(1)
    def __init__(self, big: int, medium: int, small: int) -> None:
        self.spaces = [big, medium, small]

    def add_car(self, car_type: int) -> bool:
        if self.spaces[car_type - 1] == 0:
            return False
        self.spaces[car_type - 1] -= 1
        return True
