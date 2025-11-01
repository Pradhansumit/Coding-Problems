# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(
        self, nums: List[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        lists = []
        nums = set(nums)
        curr = head
        while curr:
            if curr.val not in nums:
                lists.append(curr.val)
            curr = curr.next
        res = ListNode(lists[0])
        curr = res
        for i in range(1, len(lists)):
            curr.next = ListNode(lists[i])
            curr = curr.next
        return res
