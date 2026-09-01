from leetcode_py import ListNode


class Solution:
    # Time: O(n)
    # Space: O(n)
    def delete_duplicates_unsorted(self, head: ListNode[int] | None) -> ListNode[int] | None:
        seen: set[int] = set()
        dupes: set[int] = set()
        cur = head
        while cur is not None:
            if cur.val in seen:
                dupes.add(cur.val)
            seen.add(cur.val)
            cur = cur.next

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        cur = head
        while cur is not None:
            nxt = cur.next
            if cur.val in dupes:
                prev.next = nxt
            else:
                prev = cur
            cur = nxt
        return dummy.next
