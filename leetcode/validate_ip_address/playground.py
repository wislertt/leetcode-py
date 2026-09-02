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
from helpers import assert_valid_ip_address, run_valid_ip_address
from solution import Solution

# %%
# Example test case
query_ip = "172.16.254.1"
expected = "IPv4"

# %%
result = run_valid_ip_address(Solution, query_ip)
result

# %%
assert_valid_ip_address(result, expected)
