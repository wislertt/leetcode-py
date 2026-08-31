# Design Excel Sum Formula

**Difficulty:** Hard
**Topics:** Graph, Design, Topological Sort, Array, Hash Table, String, Matrix
**Tags:** neetcode

**LeetCode:** [Problem 631](https://leetcode.com/problems/design-excel-sum-formula/description/)

## Problem Description

Design the basic function of **Excel** and implement the function of the sum formula.

Implement the `Excel` class:

- `Excel(int height, char width)` Initializes the object with the `height` and the `width` of the sheet. The sheet is an integer matrix `mat` of size `height x width` with the row index in the range `[1, height]` and the column index in the range `['A', width]`. All the values should be **zero** initially.
- `void set(int row, char column, int val)` Changes the value at `mat[row][column]` to be `val`.
- `int get(int row, char column)` Returns the value at `mat[row][column]`.
- `int sum(int row, char column, List<String> numbers)` Sets the value at `mat[row][column]` to be the sum of cells represented by `numbers` and returns the value at `mat[row][column]`. This sum formula **should exist** until this cell is overlapped by another value or another sum formula. `numbers[i]` could be on the format:
    - `"ColRow"` that represents a single cell. For example, `"F7"` represents the cell `mat[7]['F']`.
    - `"ColRow1:ColRow2"` that represents a range of cells. The range will always be a rectangle where `"ColRow1"` represents the position of the top-left cell, and `"ColRow2"` represents the position of the bottom-right cell.

**Note:** You could assume that there will not be any circular sum reference.

## Examples

### Example 1:

```
Input
["Excel", "set", "sum", "set", "get"]
[[3, "C"], [1, "A", 2], [3, "C", ["A1", "A1:B2"]], [2, "B", 2], [3, "C"]]
Output
[null, null, 4, null, 6]

Explanation
Excel excel = new Excel(3, "C");
excel.set(1, "A", 2);
excel.sum(3, "C", ["A1", "A1:B2"]); // return 4
excel.set(2, "B", 2);
excel.get(3, "C"); // return 6
```

## Constraints

- `1 <= height <= 26`
- `'A' <= width <= 'Z'`
- `1 <= row <= height`
- `'A' <= column <= width`
- `-100 <= val <= 100`
- `1 <= numbers.length <= 5`
- `numbers[i]` has the format `"ColRow"` or `"ColRow1:ColRow2"`.
- At most `100` calls will be made to `set`, `get`, and `sum`.
