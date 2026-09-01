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
from helpers import assert_underground_system_operations, run_underground_system_operations
from solution import UndergroundSystem

# %%
# Example test case
operations = [
    "UndergroundSystem",
    "check_in",
    "check_in",
    "check_in",
    "check_out",
    "check_out",
    "check_out",
    "get_average_time",
]
inputs = [
    [],
    [45, "Leyton", 3],
    [32, "Paradise", 8],
    [27, "Leyton", 10],
    [45, "Waterloo", 15],
    [27, "Waterloo", 20],
    [32, "Cambridge", 22],
    ["Paradise", "Cambridge"],
]
expected = [None, None, None, None, None, None, None, 14.0]

# %%
result, system = run_underground_system_operations(UndergroundSystem, operations, inputs)
print(result)
system

# %%
assert_underground_system_operations(result, expected)
