# https://leetcode.com/problems/add-two-numbers/

class Solution(object):

    def getNumber(self, l1):
        total = 0
        digit = 0
        node  = l1
        while node is not None:
            total += node.val * pow(10,digit)
            digit += 1
            node   = node.next
        return total

    def createList(self, n):
        val       = n % 10
        broken_n  = int(n / 10)
        next_node = None

        if broken_n != 0:
            next_node = self.createList(broken_n)

        return ListNode(val=val, next=next_node)


    def addTwoNumbersEasy(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        return self.createList( self.getNumber(l1) + self.getNumber(l2) )

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(None)
        curr = head
        i1 = l1
        i2 = l2
        carry = 0
        while i1 is not None or i2 is not None or carry != 0:
            v1 = v2 = 0
            if i1 is not None:
                v1 = i1.val
                i1 = i1.next
            if i2 is not None:
                v2 = i2.val
                i2 = i2.next

            digit = v1 + v2 + carry
            carry = int(digit / 10)

            curr.next = ListNode(digit % 10)
            curr  = curr.next

        return head.next
