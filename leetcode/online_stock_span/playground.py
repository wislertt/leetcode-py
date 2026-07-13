# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.4
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_online_stock_span_operations, run_online_stock_span_operations
from solution import StockSpanner

# %%
# Example test case
operations = ["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
inputs = [[], [100], [80], [60], [70], [60], [75], [85]]
expected = [None, 1, 1, 1, 2, 1, 4, 6]

# %%
result = run_online_stock_span_operations(StockSpanner, operations, inputs)
result

# %%
assert_online_stock_span_operations(result, expected)
