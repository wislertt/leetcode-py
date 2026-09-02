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
from helpers import assert_ip_to_cidr, run_ip_to_cidr
from solution import Solution

# %%
# Example test case
ip = "255.0.0.7"
n = 10
expected = ["255.0.0.7/32", "255.0.0.8/29", "255.0.0.16/32"]

# %%
result = run_ip_to_cidr(Solution, ip, n)
result

# %%
assert_ip_to_cidr(result, expected)
