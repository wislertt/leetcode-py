# Accounts Merge

**Difficulty:** Medium
**Topics:** Array, Hash Table, String, Depth-First Search, Breadth-First Search, Union Find, Sorting
**Tags:** grind, grind-75

**LeetCode:** [Problem 721](https://leetcode.com/problems/accounts-merge/description/)


## Problem Description

Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

&nbsp;
Example 1:


Input: accounts = [[&quot;John&quot;,&quot;johnsmith@mail.com&quot;,&quot;john_newyork@mail.com&quot;],[&quot;John&quot;,&quot;johnsmith@mail.com&quot;,&quot;john00@mail.com&quot;],[&quot;Mary&quot;,&quot;mary@mail.com&quot;],[&quot;John&quot;,&quot;johnnybravo@mail.com&quot;]]
Output: [[&quot;John&quot;,&quot;john00@mail.com&quot;,&quot;john_newyork@mail.com&quot;,&quot;johnsmith@mail.com&quot;],[&quot;Mary&quot;,&quot;mary@mail.com&quot;],[&quot;John&quot;,&quot;johnnybravo@mail.com&quot;]]
Explanation:
The first and second John&#39;s are the same person as they have the common email &quot;johnsmith@mail.com&quot;.
The third John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [[&#39;Mary&#39;, &#39;mary@mail.com&#39;], [&#39;John&#39;, &#39;johnnybravo@mail.com&#39;], 
[&#39;John&#39;, &#39;john00@mail.com&#39;, &#39;john_newyork@mail.com&#39;, &#39;johnsmith@mail.com&#39;]] would still be accepted.


Example 2:


Input: accounts = [[&quot;Gabe&quot;,&quot;Gabe0@m.co&quot;,&quot;Gabe3@m.co&quot;,&quot;Gabe1@m.co&quot;],[&quot;Kevin&quot;,&quot;Kevin3@m.co&quot;,&quot;Kevin5@m.co&quot;,&quot;Kevin0@m.co&quot;],[&quot;Ethan&quot;,&quot;Ethan5@m.co&quot;,&quot;Ethan4@m.co&quot;,&quot;Ethan0@m.co&quot;],[&quot;Hanzo&quot;,&quot;Hanzo3@m.co&quot;,&quot;Hanzo1@m.co&quot;,&quot;Hanzo0@m.co&quot;],[&quot;Fern&quot;,&quot;Fern5@m.co&quot;,&quot;Fern1@m.co&quot;,&quot;Fern0@m.co&quot;]]
Output: [[&quot;Ethan&quot;,&quot;Ethan0@m.co&quot;,&quot;Ethan4@m.co&quot;,&quot;Ethan5@m.co&quot;],[&quot;Gabe&quot;,&quot;Gabe0@m.co&quot;,&quot;Gabe1@m.co&quot;,&quot;Gabe3@m.co&quot;],[&quot;Hanzo&quot;,&quot;Hanzo0@m.co&quot;,&quot;Hanzo1@m.co&quot;,&quot;Hanzo3@m.co&quot;],[&quot;Kevin&quot;,&quot;Kevin0@m.co&quot;,&quot;Kevin3@m.co&quot;,&quot;Kevin5@m.co&quot;],[&quot;Fern&quot;,&quot;Fern0@m.co&quot;,&quot;Fern1@m.co&quot;,&quot;Fern5@m.co&quot;]]


&nbsp;
Constraints:


	1 &lt;= accounts.length &lt;= 1000
	2 &lt;= accounts[i].length &lt;= 10
	1 &lt;= accounts[i][j].length &lt;= 30
	accounts[i][0] consists of English letters.
	accounts[i][j] (for j &gt; 0) is a valid email.

## Examples

### Example 1:

Input: accounts = [[&quot;John&quot;,&quot;johnsmith@mail.com&quot;,&quot;john_newyork@mail.com&quot;],[&quot;John&quot;,&quot;johnsmith@mail.com&quot;,&quot;john00@mail.com&quot;],[&quot;Mary&quot;,&quot;mary@mail.com&quot;],[&quot;John&quot;,&quot;johnnybravo@mail.com&quot;]]
Output: [[&quot;John&quot;,&quot;john00@mail.com&quot;,&quot;john_newyork@mail.com&quot;,&quot;johnsmith@mail.com&quot;],[&quot;Mary&quot;,&quot;mary@mail.com&quot;],[&quot;John&quot;,&quot;johnnybravo@mail.com&quot;]]
Explanation:
The first and second John&#39;s are the same person as they have the common email &quot;johnsmith@mail.com&quot;.
The third John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [[&#39;Mary&#39;, &#39;mary@mail.com&#39;], [&#39;John&#39;, &#39;johnnybravo@mail.com&#39;], 
[&#39;John&#39;, &#39;john00@mail.com&#39;, &#39;john_newyork@mail.com&#39;, &#39;johnsmith@mail.com&#39;]] would still be accepted.


Example 2:


Input: accounts = [[&quot;Gabe&quot;,&quot;Gabe0@m.co&quot;,&quot;Gabe3@m.co&quot;,&quot;Gabe1@m.co&quot;],[&quot;Kevin&quot;,&quot;Kevin3@m.co&quot;,&quot;Kevin5@m.co&quot;,&quot;Kevin0@m.co&quot;],[&quot;Ethan&quot;,&quot;Ethan5@m.co&quot;,&quot;Ethan4@m.co&quot;,&quot;Ethan0@m.co&quot;],[&quot;Hanzo&quot;,&quot;Hanzo3@m.co&quot;,&quot;Hanzo1@m.co&quot;,&quot;Hanzo0@m.co&quot;],[&quot;Fern&quot;,&quot;Fern5@m.co&quot;,&quot;Fern1@m.co&quot;,&quot;Fern0@m.co&quot;]]
Output: [[&quot;Ethan&quot;,&quot;Ethan0@m.co&quot;,&quot;Ethan4@m.co&quot;,&quot;Ethan5@m.co&quot;],[&quot;Gabe&quot;,&quot;Gabe0@m.co&quot;,&quot;Gabe1@m.co&quot;,&quot;Gabe3@m.co&quot;],[&quot;Hanzo&quot;,&quot;Hanzo0@m.co&quot;,&quot;Hanzo1@m.co&quot;,&quot;Hanzo3@m.co&quot;],[&quot;Kevin&quot;,&quot;Kevin0@m.co&quot;,&quot;Kevin3@m.co&quot;,&quot;Kevin5@m.co&quot;],[&quot;Fern&quot;,&quot;Fern0@m.co&quot;,&quot;Fern1@m.co&quot;,&quot;Fern5@m.co&quot;]]

## Constraints

- 1 &lt;= accounts.length &lt;= 1000
- 2 &lt;= accounts[i].length &lt;= 10
- 1 &lt;= accounts[i][j].length &lt;= 30
- accounts[i][0] consists of English letters.
- accounts[i][j] (for j &gt; 0) is a valid email.


