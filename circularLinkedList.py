class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        if self.head: return False
        print('Circular list is empty')
        return True
    
    def show(self):
        lst = []
        if not self.isEmpty():      
            lst.append(self.head.value)      
            curNode = self.head.next
            while curNode != self.head:
                lst.append(curNode.value)
                curNode = curNode.next
        print(lst)
            

    
    def addNode(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            return
        curNode = self.head
        while curNode.next != self.head:
            curNode = curNode.next
        curNode.next = newNode
        newNode.next = self.head
    
    def getMiddleNode(self):
        ptrone, ptrtwo = self.head, self.head
        while True:
            try:
                ptrone = ptrone.next
                ptrtwo = ptrtwo.next.next
            except: break
        return ptrone
        
         

cll = CircularLinkedList()
cll.addNode(5)        
cll.addNode(9)        
cll.addNode(654)        
cll.addNode(45)        
cll.addNode(552)        

cll.show()

