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
from helpers import assert_most_visited_pattern, run_most_visited_pattern
from solution import Solution

# %%
# Example test case
username = ["joe", "joe", "joe", "james", "james", "james", "james", "mary", "mary", "mary"]
timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
website = ["home", "about", "career", "home", "cart", "maps", "home", "home", "about", "career"]
expected = ["home", "about", "career"]

# %%
result = run_most_visited_pattern(Solution, username, timestamp, website)
result

# %%
assert_most_visited_pattern(result, expected)
