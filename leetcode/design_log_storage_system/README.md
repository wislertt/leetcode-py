# Design Log Storage System

**Difficulty:** Medium
**Topics:** Design, Hash Table, String, Ordered Set
**Tags:** neetcode

**LeetCode:** [Problem 635](https://leetcode.com/problems/design-log-storage-system/description/)

## Problem Description

You are given several logs, where each log contains a unique ID and timestamp. Timestamp is a string that has the following format: `Year:Month:Day:Hour:Minute:Second`, for example, `2017:01:01:23:59:59`. All domains are zero-padded decimal numbers.

Implement the `LogSystem` class:

- `LogSystem()` Initializes the `LogSystem` object.
- `void put(int id, string timestamp)` Stores the given log `(id, timestamp)` in your storage system.
- `int[] retrieve(string start, string end, string granularity)` Returns the IDs of the logs whose timestamps are within the range from `start` to `end` inclusive. `start` and `end` all have the same format as `timestamp`, and `granularity` means how precise the range should be (i.e. to the exact `Day`, `Minute`, etc.).

## Examples

### Example 1:

```
Input
["LogSystem", "put", "put", "put", "retrieve", "retrieve"]
[[1, "2017:01:01:23:59:59"], ...]
Output
[null, null, null, null, [3, 2, 1], [2, 1]]

Explanation
LogSystem logSystem = new LogSystem();
logSystem.put(1, "2017:01:01:23:59:59");
logSystem.put(2, "2017:01:01:22:59:59");
log.put(3, "2016:01:01:00:00:00");
logSystem.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Year"); // return [3,2,1], all logs between 2016 and 2017.
logSystem.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Hour"); // return [2,1]
```

## Constraints

- `1 <= id <= 500`
- `2000 <= Year <= 2017`
- `1 <= Month <= 12`
- `1 <= Day <= 31`
- `0 <= Hour <= 23`
- `0 <= Minute, Second <= 59`
- `granularity` is one of the values `["Year", "Month", "Day", "Hour", "Minute", "Second"]`.
- At most `500` calls will be made to `put` and `retrieve`.
