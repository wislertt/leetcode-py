# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.5
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_traffic_light, run_traffic_light
from solution import TrafficLight

# %%
# Example test case
operations = [
    "TrafficLight",
    "car_arrived",
    "car_arrived",
    "car_arrived",
    "car_arrived",
    "car_arrived",
]
inputs = [[], [1, 1, 2], [3, 1, 1], [5, 1, 2], [2, 2, 4], [4, 2, 3]]
expected = [
    "Car 1 Has Passed Road A In Direction 2",
    "Car 3 Has Passed Road A In Direction 1",
    "Car 5 Has Passed Road A In Direction 2",
    "Traffic Light On Road B Is Green",
    "Car 2 Has Passed Road B In Direction 4",
    "Car 4 Has Passed Road B In Direction 3",
]

# %%
result, light = run_traffic_light(TrafficLight, operations, inputs)
print(result)
light

# %%
assert_traffic_light(result, expected)
