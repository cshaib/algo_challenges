# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        val1 = []
        val2 = []
        num1 = ''
        num2 = ''
        
        # collect node values
        while (l1 != None):
            val1.append(str(l1.val))
            l1 = l1.next
        
        while (l2 != None):
            val2.append(str(l2.val))
            l2 = l2.next
            
        # reverse list 
        val1 = val1[::-1]
        val2 = val2[::-1]
        
        # create int 
        for x in val1:
            num1 += x
        for y in val2:
            num2 += y
        
        # find final sum
        final_val = int(num1) + int(num2)

        # return list with reverse
        to_return = map(int, str(final_val))
        
        # map answer back to list, reverse 
        f = list(to_return)[::-1]
        
        return f