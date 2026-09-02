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
from helpers import assert_logger_rate_limiter, run_logger_rate_limiter
from solution import Logger

# %%
# Example test case
operations = ["Logger", "should_print_message", "should_print_message"]
inputs = [[], [1, "foo"], [2, "bar"]]
expected = [None, True, True]

# %%
result, logger = run_logger_rate_limiter(Logger, operations, inputs)
print(result)
logger

# %%
assert_logger_rate_limiter(result, expected)
