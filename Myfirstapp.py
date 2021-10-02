# Python3 program to merge sort of linked list 
  
# create Node using class Node. 
class Node: 
    def __init__(self, dataValue): 
        self.dataValue = dataValue
        self.nextNode = None
  
class LinkedList: 
    def __init__(self): 
        self.headNode = None
      
    # push new value to linked list 
    # using append method 
    def append(self, newValue): 
          
        # Allocate new node 
        newNode = Node(newValue) 
          
        # if head is None, initialize it to new node 
        if self.headNode is None: 
            self.headNode = newNode 
            return
        currentNode = self.headNode
        while currentNode.nextNode is not None: 
            currentNode = currentNode.nextNode
              
        # Append the new node at the end 
        # of the linked list 
        currentNode.nextNode = newNode  
          
    def sortedMerge(self, leftNode, rightNode): 
        resultNode = None
          
        # Base cases 
        if leftNode == None: 
            return rightNode 
        if rightNode == None: 
            return leftNode 
              
        # pick either a or b and recur.. 
        if leftNode.dataValue <= rightNode.dataValue: 
            resultNode = leftNode 
            resultNode.nextNode = self.sortedMerge(leftNode.nextNode, rightNode) 
        else: 
            resultNode = rightNode 
            resultNode.nextNode = self.sortedMerge(leftNode, rightNode.nextNode) 
        return resultNode 
      
    def mergeSort(self, headNode): 
          
        # Base case if head is None 
        if headNode == None or headNode.nextNode == None: 
            return headNode
  
        # get the middle of the list  
        middleNode = self.getMiddle(headNode) 
        nexttomiddleNode = middleNode.nextNode
  
        # set the next of middle node to None 
        middleNode.nextNode = None
  
        # Apply mergeSort on left list  
        left = self.mergeSort(headNode) 
          
        # Apply mergeSort on right list 
        right = self.mergeSort(nexttomiddleNode) 
  
        # Merge the left and right lists  
        sortedlist = self.sortedMerge(left, right) 
        return sortedlist  
      
    # Utility function to get the middle  
    # of the linked list  
    def getMiddle(self, headNode): 
        if (headNode == None): 
            return headNode
  
        slowNode = headNode 
        fastNode = headNode 
  
        while (fastNode.nextNode != None and 
               fastNode.nextNode.nextNode != None): 
            slowNode = slowNode.nextNode
            fastNode = fastNode.nextNode.nextNode
              
        return slowNode 
          
# Utility function to print the linked list  
def printList(headNode): 
    if headNode is None: 
        print(' ') 
        return
    curr_node = headNode 
    while curr_node: 
        print(curr_node.dataValue, end = " ") 
        curr_node = curr_node.nextNode
    print(' ') 
      
