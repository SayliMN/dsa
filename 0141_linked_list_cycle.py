class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def linkedListCycle(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next #link to the next node object
            fast = fast.next.next #
            if slow == fast:
                return True
        return False

def build_linked_list_with_cycle(values, pos):
    dummy = ListNode()
    curr = dummy
    cycle_node = None
    for i, v in enumerate(values):
        curr.next = ListNode(v)
        curr = curr.next
        if i == pos:
            cycle_node = curr

    if pos != i:
        curr.next = cycle_node

    return dummy.next


if __name__ == "__main__":
    s = Solution()
    head = [3, 2, 0, -4]
    pos = 1
    ss = build_linked_list_with_cycle(head, pos)
    print(s.linkedListCycle(ss))

    # s = Solution()
    # head = build_linked_list_with_cycle([3, 2, 0, -4], pos=1)
    # print(s.linkedListCycle(head))