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
from helpers import assert_restore_ip_addresses, run_restore_ip_addresses
from solution import Solution

# %%
# Example test case
s = "25525511135"
expected = ["255.255.11.135", "255.255.111.35"]

# %%
result = run_restore_ip_addresses(Solution, s)
result

# %%
assert_restore_ip_addresses(result, expected)
