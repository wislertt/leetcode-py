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
from helpers import assert_earliest_acq, run_earliest_acq
from solution import Solution

# %%
# Example test case
logs = [
    [20190101, 0, 1],
    [20190104, 3, 4],
    [20190107, 2, 3],
    [20190211, 1, 5],
    [20190224, 2, 4],
    [20190301, 0, 3],
    [20190312, 1, 2],
    [20190322, 4, 5],
]
n = 6
expected = 20190301

# %%
result = run_earliest_acq(Solution, logs, n)
result

# %%
assert_earliest_acq(result, expected)
