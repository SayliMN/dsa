class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        node = dummy
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        node.next = list1 or list2

        return dummy.next


def build_linked_list(values):
    """Convert a Python list into a linked list."""
    dummy = ListNode()
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def print_linked_list(node):
    """Convert linked list back into a Python list for easy printing."""
    values = []
    while node:
        values.append(node.val)
        node = node.next
    return values


if __name__ == "__main__":
    s = Solution()
    list1 = build_linked_list([1,2,3])
    list2 = build_linked_list([1,3,4])
    merged = s.mergeTwoLists(list1, list2)
    print(print_linked_list(merged))