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
from helpers import assert_log_storage, run_log_storage
from solution import LogSystem

# %%
# Example test case
operations = ["LogSystem", "put", "retrieve"]
inputs = [[], [1, "2017:01:01:23:59:59"], ["2016:01:01:01:01:01", "2017:01:01:23:00:00", "Year"]]
expected = [None, None, [1]]

# %%
result, log_system = run_log_storage(LogSystem, operations, inputs)
print(result)
log_system

# %%
assert_log_storage(result, expected)
