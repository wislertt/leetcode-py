# Text Justification

**Difficulty:** Hard
**Topics:** Array, String, Simulation
**Tags:** neetcode

**LeetCode:** [Problem 68](https://leetcode.com/problems/text-justification/description/)

## Problem Description

Given an array of strings `words` and a width `max_width`, format the text such that each line has exactly `max_width` characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces `' '` when necessary so that each line has exactly `max_width` characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

**Note:**

- A word is defined as a character sequence consisting of non-space characters only.
- Each word's length is guaranteed to be greater than 0 and not exceed `max_width`.
- The input array `words` contains at least one word.

## Examples

### Example 1:

```
Input: words = ["This", "is", "an", "example", "of", "text", "justification."], max_width = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
```

### Example 2:

```
Input: words = ["What","must","be","acknowledgment","shall","be"], max_width = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.
```

### Example 3:

```
Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], max_width = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
```

## Constraints

- 1 <= words.length <= 300
- 1 <= words[i].length <= 20
- words[i] consists of only English letters and symbols.
- 1 <= max_width <= 100
- words[i].length <= max_width
