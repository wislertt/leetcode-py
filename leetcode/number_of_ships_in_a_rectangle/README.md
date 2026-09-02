# Number of Ships in a Rectangle

**Difficulty:** Hard
**Topics:** Array, Divide and Conquer, Interactive
**Tags:** neetcode

**LeetCode:** [Problem 1274](https://leetcode.com/problems/number-of-ships-in-a-rectangle/description/)

## Problem Description

(This problem is an **interactive problem**.)

Each ship is located at an integer point on the sea represented by a cartesian plane, and each integer point may contain at most 1 ship.

You have a function `Sea.has_ships(top_right, bottom_left)` which takes two points as arguments and returns `true` if there is at least one ship in the rectangle represented by the two points, including on the boundary.

Given two points: the top right and bottom left corners of a rectangle, return the number of ships present in that rectangle. It is guaranteed that there are **at most 10 ships** in that rectangle.

Submissions making **more than 400 calls** to `has_ships` will be judged **Wrong Answer**. Also, any solutions that attempt to circumvent the judge will be disqualified.

The API is:

```
class Sea:
    def has_ships(self, top_right: 'Point', bottom_left: 'Point') -> bool: ...

class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
```

## Examples

### Example 1:

![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1200-1299/1274.Number%20of%20Ships%20in%20a%20Rectangle/images/1445_example_1.png)

```
Input:
ships = [[1,1],[2,2],[3,3],[5,5]], topRight = [4,4], bottomLeft = [0,0]
Output: 3
Explanation: From [0,0] to [4,4] we can count 3 ships within the range.
```

### Example 2:

```
Input:
ships = [[1,1],[2,2],[3,3]], topRight = [1000,1000], bottomLeft = [0,0]
Output: 3
```

## Constraints

- On the input `ships` is only given to initialize the map internally. You must solve this problem "blindfolded". In other words, you must find the answer using the given `has_ships` API, without knowing the `ships` position.
- `0 <= bottomLeft[0] <= topRight[0] <= 1000`
- `0 <= bottomLeft[1] <= topRight[1] <= 1000`
- `topRight != bottomLeft`
