# https://leetcode.com/problems/merge-k-sorted-lists/

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        merged_first   = None
        merged_current = None

        while len(lists):
            lowest_list = 0
            lowest_val  = 2**31
            found = False

            for i,l in enumerate(lists):
                if l is not None and l.val < lowest_val:
                    lowest_val = l.val
                    lowest_list = i
                    found = True

            if found:
                if merged_first is None:
                    merged_first = ListNode(val=lowest_val)
                    merged_current = merged_first
                else:
                    merged_current.next = ListNode(val=lowest_val)
                    merged_current = merged_current.next

                if lists[lowest_list]:
                    lists[lowest_list] = lists[lowest_list].next

            if lists[lowest_list] == None:
                lists.remove(None)

        return merged_first