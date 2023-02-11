
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
