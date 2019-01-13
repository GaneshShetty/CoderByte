class Stack:

    def __init__(self):
       self.stack=[]
       self.top=0

    def push(self,data):
        self.top+=1
        self.stack.append(data)
        print "Element inserted is " + str(data)


    def pop(self):
       return self.stack.pop()


    def display(self):
        print "Displaying the elements from stack"
        curr=len(self.stack)-1
        while curr>-1:
            print self.stack[curr],
            curr-=1
        print "\n"

s1=Stack()
s1.push(10)
s1.push(20)
s1.push(30)

s1.display()

print "Poping element " + str(s1.pop())

s1.display()