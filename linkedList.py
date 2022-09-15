class Node:
    def __init__(self, value=None):
        self.value =  value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def addAtStart(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            return
        prvHead = self.head
        self.head = newNode
        self.head.next = prvHead

    def addNode(self, value):
        newNode = Node(value)
        
        if self.head is None:
            self.head = newNode
            return

        curNode = self.head
        while curNode.next:
            curNode = curNode.next
        curNode.next = newNode
    
    def addLst(self, lst):
        nodeLst = []
        headNode = Node(lst[0])
        nodeLst.append(headNode)
        for i in range(1, len(lst)):
            ele = lst[i]
            newNode = Node(ele)
            lastNode = nodeLst[-1]
            lastNode.next = newNode
            nodeLst.append(newNode)
            
        if self.head is None:
            self.head = nodeLst[0]
            return
        curNode = self.head
        while curNode.next:
            curNode = curNode.next
        curNode.next = nodeLst[0]
        self.showNode()        
        

    def _showNodeRec(self, node):
        if node:
            print(node.value, end="->")
            self._showNodeRec(node.next)

    def showNodeRec(self):
        ans = self._showNodeRec(self.head)
        print(ans)
        
    def showNode(self):
        if self.head is None:
            print('Linked list is empty')
            return
        lst = []
        curNode = self.head
        while curNode:
            lst.append(curNode.value)
            curNode = curNode.next
        print(lst)
    
    def getMiddleNodeValue(self):
        ptrone = self.head
        ptrtwo = self.head
        if self.head is None:
            print('Linked list is emtpy.')
            return
        while True:
            try:
                ptrtwo = ptrtwo.next.next
                ptrone = ptrone.next
            except:
                break
        print('Middle node value is', ptrone.value)
    
    def _isEmpty(self):
        if self.head: return False
        print("Linked list is empty")
        return True
    
    # def reverseLinkList(self):
    #     if self._isEmpty(): return
    #     curNode = self.head
    #     reversedLinkedList = LinkedList()
    #     while curNode:
    #         reversedLinkedList.addAtStart(curNode.value)
    #         curNode = curNode.next
    #     reversedLinkedList.showNode()
    #     return reversedLinkedList

    def reverseLinkList(self):
        if self._isEmpty(): return
        prvNode = None
        curNode = self.head

        while curNode:
            nxtNode = curNode.next
            curNode.next = prvNode
            prvNode = curNode
            curNode = nxtNode

        self.head = prvNode
    
    def delNode(self, ind):
        cur = self.head
        prv = self.head
        counter = 0
        while not (cur.next==None or counter==ind):
            prv = cur
            cur = cur.next
            counter += 1
        if counter!=ind:
            print('Index out of range')
            return
        prv.next = cur.next
        print('Node deleted')
        self.showNode()
    
    def insertNode(self, value, pos=None):    
        newNode = Node(value)
        if pos is None:
            self.addNode(value)
        else:
            counter = 0
            cur = self.head
            prv = self.head
            while cur.next!=None and counter!=pos:
                prv = cur
                cur = cur.next
                counter += 1
            prv.next = newNode
            newNode.next = cur
        self.showNode()


ll = LinkedList()

ll.addNode(5)
ll.addNode(50)
ll.addNode(54)
ll.addNode(565)
ll.addNode(3000)
ll.showNodeRec()

ll.reverseLinkList()

ll.showNodeRec()


###############################################################################################################
###############################################################################################################
l1 = LinkedList()
l1.addLst([3,5,6,9,18,20,55,58])

l2 = LinkedList()
l2.addLst([1])


# merge two sorted linked list to get new sorted list
def sortedMerge(l1, l2):
    lone = l1.head
    ltwo = l2.head
    prv = None
    while lone and ltwo:
        if lone.value < ltwo.value:
            if prv is  not None:
                prv.next = lone
            prv = lone
            lone = lone.next
        else:
            if prv is  not None:
                prv.next = ltwo
            prv = ltwo
            ltwo = ltwo.next
    if lone is not None:
        prv.next = lone
    if ltwo is not None:
        prv.next = ltwo
    if l1.head.value < l2.head.value:
        return l1
    return l2

sortedLst = sortedMerge(l1, l2)
sortedLst.showNode()