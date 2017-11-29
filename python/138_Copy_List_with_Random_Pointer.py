# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return 
        
        tbl = {}
        node = head
        while node:
            tbl[node] = RandomListNode(node.label)
            node = node.next
            
        node = head
        while node:
            if node.next:
                tbl[node].next = tbl[node.next]
            if node.random:
                tbl[node].random = tbl[node.random]
            node = node.next
            
        return tbl[head]        