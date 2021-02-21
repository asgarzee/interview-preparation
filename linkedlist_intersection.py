'''
Write a function to find the intersection between two singly-linked lists.
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    nodeA_set = set()

    currentA = headA
    while(currentA):
        nodeA_set.add(currentA)
        currentA = currentA.next
    currentB = headB
    while(currentB):
        if currentB in nodeA_set:
            return currentB
        currentB = currentB.next

    return None
