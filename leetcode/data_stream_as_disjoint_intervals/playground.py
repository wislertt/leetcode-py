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
from helpers import assert_data_stream_as_disjoint_intervals, run_data_stream_as_disjoint_intervals
from solution import SummaryRanges

# %%
# Example test case
operations = ["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals"]
inputs = [[], [1], [], [3], []]
expected = [None, None, [[1, 1]], None, [[1, 1], [3, 3]]]

# %%
result = run_data_stream_as_disjoint_intervals(SummaryRanges, operations, inputs)
result

# %%
assert_data_stream_as_disjoint_intervals(result, expected)
