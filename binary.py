class Node:

    def __init__(self,dataval=None,):
        self.dataval=dataval
        self.left=None
        self.right=None


class BST:

    def __init__(self):
        self.root=Node()

    def addnode(self,val):
        if self.root.dataval ==None:
            self.root=Node(val)

        else:
            newnode=Node(val)
            curr=self.root
            while curr:
                if curr.dataval > val:
                    if curr.left is not None:
                        curr=curr.left
                    else:
                        curr.left=newnode
                        return
                else:
                    if curr.right is not None:
                        curr=curr.right
                    else:
                        curr.right=newnode
                        return

    def display(self,node):
        if node.left:
            self.display(node.left)
        print node.dataval
        if node.right:
            self.display(node.right)

    def childcount(self,node):
        count=0
        if node.left:
            count+=1
        if node.right:
            count+=1
        return count

    def FindParent(self,val,node,parent=None):

        #print "val " + str(val) + " node is " + str(node.dataval) + " parent " + str(parent)
        if node.dataval==val:
            #print " found it is " + str(node.dataval) + " parent is " + str(parent.dataval)
            return parent,node

        if node.dataval>val:
            return self.FindParent(val,node.left,node)
        else:
           return  self.FindParent(val,node.right,node)

    def removenode(self,val,node):
        if self.root.dataval is None:
            print "Tree is empty"
            return

 





BT=BST()
BT.addnode(10)
BT.addnode(5)
BT.addnode(15)
BT.addnode(13)
#BT.display(BT.root)


p,c= BT.FindParent(13,BT.root)

print BT.childcount(BT.root)
print "child " + str(c.dataval) + " parent "+ str(p.dataval)
