# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.1
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_detect_cycle, run_detect_cycle
from solution import Solution

# %%
# Example test case
head_vals: list[int] = [3, 2, 0, -4]
pos: int = 1
expected: int = 1

# %%
result = run_detect_cycle(Solution, head_vals, pos)
print(f"Cycle starts at index: {result}")
result

# %%
assert_detect_cycle(result, expected)
