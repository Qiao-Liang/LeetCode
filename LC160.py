"""
Intersection of Two Linked Lists
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def intersect(headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: ListNode
    """
    lengthA = 0
    lengthB = 0
    nodeA = headA
    nodeB = headB
    
    while nodeA:
        nodeA = nodeA.next
        lengthA += 1
    while nodeB:
        nodeB = nodeB.next
        lengthB += 1
    
    nodeA = headA
    nodeB = headB
    if lengthA > lengthB:
        n = lengthA - lengthB
        while n > 0:
            nodeA = nodeA.next
            n -= 1
    elif lengthA < lengthB:
        n = lengthB - lengthA
        while n > 0:
            nodeB = nodeB.next
            n -= 1
    
    while nodeA and nodeB:
        if nodeA != nodeB:
            nodeA = nodeA.next
            nodeB = nodeB.next
        else:
            return nodeA
    
    return None

node = ListNode(1)

print intersect(node, node)