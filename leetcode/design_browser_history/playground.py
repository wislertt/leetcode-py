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
from helpers import assert_browser_history_operations, run_browser_history_operations
from solution import BrowserHistory

# %%
# Example test case
operations = [
    "BrowserHistory",
    "visit",
    "visit",
    "visit",
    "back",
    "back",
    "forward",
    "visit",
    "forward",
    "back",
    "back",
]
inputs = [
    ["leetcode.com"],
    ["google.com"],
    ["facebook.com"],
    ["youtube.com"],
    [1],
    [1],
    [1],
    ["linkedin.com"],
    [2],
    [2],
    [7],
]
expected = [
    None,
    None,
    None,
    None,
    "facebook.com",
    "google.com",
    "facebook.com",
    None,
    "linkedin.com",
    "google.com",
    "leetcode.com",
]

# %%
result, history = run_browser_history_operations(BrowserHistory, operations, inputs)
print(result)
history

# %%
assert_browser_history_operations(result, expected)
