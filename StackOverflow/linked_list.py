class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def create_new_node(res, l):
    res.next = ListNode(l.val)
    l=l.next
    res=res.next
    return l

ll = ListNode(1)
ll.next = ListNode(2)

res = ListNode(ll.val)

current = ll
while current:
    print(current.val)
    current = create_new_node(res, current)

current = res
while current: 
    print(current.val)
    current = current.next

 