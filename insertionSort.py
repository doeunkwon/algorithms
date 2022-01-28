def insertionSort(a):
    for i in range(len(a)):
        order(a,i)
    return a

def order(a, i):
    temp = a[i]
    j = i
    while (j > 0) and (a[j-1] > temp):
        a[j] = a[j-1]
        j -= 1
    a[j] = temp
