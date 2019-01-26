'''
from GeeksforGeeks

Smallest subarray containing minimum and maximum values

Given an array A of size N. The task is to find the length of smallest subarray which contains both maximum and minimum values.

Examples:

Input : A[] = {1, 5, 9, 7, 1, 9, 4}
Output : 2
subarray {1, 9} has both maximum and minimum value.

Input : A[] = {2, 2, 2, 2}
Output : 1
2 is both maximum and minimum here.


'''


def minmax(a):
    min=max=a[0]
    for i in range(1, len(a)):
        if min>a[i]:
            min=a[i]
        if max<a[i]:
            max=a[i]

    return set([min,max])
    '''
    if min==max:
        return [min]
    else:

        return [min,max]
    '''
a=[2, 2, 2, 2]
a1=[1, 5, 9, 7, 1, 9, 4]
print  len(minmax(a1))