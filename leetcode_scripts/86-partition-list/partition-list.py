# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        """
        Idea: since it is partition. Then i suppose it is ok to do a split function to 2 seperate linked lists then have them joined together
        """
        #base case: if HEAD IS NOTHING
        if not head:
            return head
        count = 0
        length = head
        while length:
            length = length.next
            count += 1
        if count == 1:
            return head
        def partitionsplit(linkedlist):
            less = None
            more = None
            curr = linkedlist
            while curr:
                val = curr.val
                if val < x and less == None:
                    temp = ListNode(val)
                    less = temp
                    less.next = None
                    curr = curr.next
                elif val < x:
                    temp = ListNode(val)
                    temp.next = None
                    add = less
                    while add.next:
                        add = add.next
                    add.next = temp
                    curr = curr.next
                elif val >= x and more == None:
                    temp = ListNode(val)
                    temp.next = None
                    more = temp
                    curr = curr.next
                else:
                    temp = ListNode(val)
                    temp.next = None
                    add = more
                    while add.next:
                        add = add.next
                    add.next = temp
                    curr = curr.next
                #print(less,more)
            return less, more
        def addtogether(linklist1, linklist2):
            temp1 = linklist1
            while temp1.next:
                temp1 = temp1.next
            temp1.next = linklist2
            return linklist1
        less, more = partitionsplit(head)

        #forgot to add. If either less or more is empty. Return just the other one
        if not less:
            return more
        elif not more:
            return less
        else:
            return addtogether(less,more)


        