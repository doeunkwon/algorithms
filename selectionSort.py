def selectionSort(l):
     for i in range(len(l)):
         min = findMin(l,i)
         swap(l, i, min)
     return l

def findMin(l,i):
    val, ind = l[i], i
    for j in range(i, len(l)):
        if l[j] <= val:
            val, ind = l[j], j
    return ind

def swap(l, a, b):
    l[a], l[b] = l[b], l[a]
