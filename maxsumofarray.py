# max and min of a subarray Kadane’s Algorithm:

def maxsum(a):
    curmax=golmax=a[0]
    for i in range(1,len(a)):
        curmax=max(a[i],a[i]+curmax)
        golmax=max(curmax,golmax)
    return golmax


def minsum(a):
    curmin=golmin=a[0]
    for i in range(1,len(a)):
        curmin=min(a[i],a[i]+curmin)
        golmin=min(curmin,golmin)
    return golmin

a=[-2,-3,4,-1,-2,1,5,-3]
a1=[3, -4, 2, -3, -1, 7, -5]

print "max sum is " + str(maxsum(a))
print "min sum is " + str(minsum(a1))