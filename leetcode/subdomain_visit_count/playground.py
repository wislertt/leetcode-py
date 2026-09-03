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
from helpers import assert_subdomain_visits, run_subdomain_visits
from solution import Solution

# %%
# Example test case
cpdomains = ["9001 discuss.leetcode.com"]
expected = ["9001 com", "9001 discuss.leetcode.com", "9001 leetcode.com"]

# %%
result = run_subdomain_visits(Solution, cpdomains)
result

# %%
assert_subdomain_visits(result, expected)
