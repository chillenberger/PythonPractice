# 24 leetCode 
# Given a linked list, swap every two adjacent nodes and return its head. 
# You must solve the problem without modifying the values in the list's 
# nodes (i.e., only nodes themselves may be changed.)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val 
        self.next = next

    @staticmethod
    def showRest(node):
        rsp = []
        currentNode = node
        while currentNode:
            rsp.append(currentNode.val)
            currentNode = currentNode.next
        print(rsp)

    @staticmethod
    def makeDefaultLL(val):
        head = ListNode(1)
        currentNode = head
        for i in range(val):
            newNode = ListNode(currentNode.val+1)
            currentNode.next = newNode 
            currentNode = newNode
        return head


class Solution:
    @classmethod
    def swapPairs(cls, head):
        try: 
            head = cls.swapFirst(head)
        except: 
            return head
        
        try: 
            preNode = head.next
            currentNode = preNode.next 
            postNode = currentNode.next
        except: 
            return head 

        while currentNode and postNode:
            ListNode.showRest(head)
            preNode, currentNode, postNode = cls.swapTwo(preNode, currentNode, postNode)
            print(preNode.val, currentNode.val, postNode.val)
            try: 
                preNode = preNode.next.next
                currentNode = preNode.next 
                postNode = currentNode.next
            except: 
                break
        
        return head

    @staticmethod
    def swapTwo(preNode, currentNode, postNode):
        preNode.next = postNode 
        currentNode.next = postNode.next 
        postNode.next = currentNode
        return preNode, currentNode, postNode

    @staticmethod 
    def swapFirst(head):
        postNode = head.next 

        head.next = postNode.next 
        postNode.next = head 
        head = postNode 
        return head





def test_swapPairs():
    head = ListNode.makeDefaultLL(11)
    ListNode.showRest(head)

    node1 = head
    node2 = head.next
    node3 = head.next.next

    head = Solution.swapPairs(head)
    ListNode.showRest(head)


if __name__ == '__main__':
    test_swapPairs()

