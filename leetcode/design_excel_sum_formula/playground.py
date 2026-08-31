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
from helpers import assert_excel_sum_formula, run_excel_sum_formula
from solution import Excel

# %%
# Example test case
operations = ["Excel", "set", "sum", "set", "get"]
inputs = [[3, "C"], [1, "A", 2], [3, "C", ["A1", "A1:B2"]], [2, "B", 2], [3, "C"]]
expected = [None, None, 4, None, 6]

# %%
result, excel = run_excel_sum_formula(Excel, operations, inputs)
print(result)
excel

# %%
assert_excel_sum_formula(result, expected)
