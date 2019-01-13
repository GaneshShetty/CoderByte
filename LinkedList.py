class Node:

    def __init__(self,dataval=None):
        self.value=dataval
        self.next=None



class LinkedList:

    def __init__(self):
        self.root=None

    def addnode(self,nodeval):
        if self.root == None:
            self.root=Node(nodeval)
        else:
            curr=self.root
            while curr.next:
                curr=curr.next
            curr.next=Node(nodeval)
        print "Node added to list is " + str(nodeval)
        return

    def delnode(self,nodeval):
        flag=0
        if self.root == None:
            print "List is empty"
            return
        curr=self.root
        prev=None
        while curr:
            if curr.value== nodeval:
                flag=1
                break
            else:
                prev=curr
                curr=curr.next

        if flag==1:
            if curr.next:
                prev.next=curr.next
                del curr

            else:
                if prev:
                    prev.next=None
                else:
                    del curr
            print "Node deleted  is" + str(nodeval)
        else:
            print "Node not found"

    def printnode(self):
        curr=self.root
        while curr:
            print curr.value
            curr=curr.next
            #print self.node.value


L1= LinkedList()
L1.delnode(10)

L1.addnode(10)
L1.printnode()

L1.delnode(10)

L1.addnode(20)
L1.addnode(30)

L1.delnode(20)
L1.printnode()