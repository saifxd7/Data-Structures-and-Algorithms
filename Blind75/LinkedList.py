
# ---------------------Reverse a LinkedList----------------------------
def reverseList(head):
    # prev, curr = None, head

    # while curr:
    #     temp = curr.next
    #     curr.next = prev
    #     prev = curr
    #     curr = temp

    # return prev

    if not head:
        return None

    newhead = head

    if head.next:
        newhead = reverseList(head.next)
        head.next.next = head

    head.next = None

    return newhead


# ---------------------------------Merge two sorted lists-----------------------
def mergeTwoLists(list1, list2):

    # tail = dummy = ListNode()
    # while list2 and list1:
    #     if list1.val < list2.val:
    #         tail.next = list1
    #         list1 = list1.next
    #     else:
    #         tail.next = list2
    #         list2 = list2.next
    #     tail = tail.next

    # if list1:
    #     tail.next = list1
    # elif list2:
    #     tail.next = list2

    # return dummy.next

    if list1 == None:
        return list2
    if list2 == None:
        return list1

    if list1.val < list2.val:
        list1.next = mergeTwoLists(list1.next, list2)
        return list1
    else:
        list2.next = mergeTwoLists(list1, list2.next)
        return list2


# --------------------------------- Reorder list -------------------------
def reorderList(head):
    """
    Do not return anything, modify head in-place instead.
    """
    # finding middle
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # reversing list from second half
    second = slow.next
    prev = slow.next = None
    while second:
        temp = second.next
        second.next = prev
        prev = second
        second = temp

    # merging both two halfs
    first, second = head, prev
    while second:
        temp1, temp2 = first.next, second.next
        first.next = second
        second.next = temp1
        first, second = temp1, temp2


# ----------------------------------------- Remove Nth node from end of list---------------------------------
class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


def removeNthFromEnd(head, n):
    dummy = ListNode(0, head)
    left = dummy
    right = head

    while n > 0:
        right = right.next
        n -= 1

    while right:
        left = left.next
        right = right.next

    # delete
    left.next = left.next.next
    return dummy.next


# ----------------------------- LinkedList Cycle ------------------------------
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(head) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

# ------------------------------ Merge K Sorted Lists ---------------------


def mergeKLists(lists):
    if len(lists) == 0:
        return None

    while len(lists) > 1:
        mergedLists = []
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if (i + 1) < len(lists) else None
            mergedLists.append(mergeList(l1, l2))
        lists = mergedLists
    return lists[0]


def mergeList(self, l1, l2):
    dummy = ListNode()
    tail = dummy

    while l1 and l2:

        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    if l1:
        tail.next = l1
    if l2:
        tail.next = l2

    return dummy.next
