def bubblesort(a):

    # Swap the elements to arrange  in ascending order
    for i in range(len(a)-1,0,-1):
        for j in range(i):
            if a[j]>a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp


# swap the elements in descending
def desending_bubblsort(a):
    for i in range(len(a)-1,0,-1):
        for j in range(i):
            if a[j]<a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp



def reverse_bubble(a):
    for i in range(len(a)-1,0,-1):
        for j in range(i,0,-1):
            if a[j]<a[j-1]:
                temp=a[j]
                a[j]=a[j-1]
                a[j-1]=temp


array = [19,2,31,45,6,11,121,27]
reverse_bubble(array)
print(array)
