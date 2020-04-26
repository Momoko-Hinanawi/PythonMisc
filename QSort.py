def swap(arr,i,j):
    k = arr[i]
    arr[i] = arr[j]
    arr[j] = k
pass

def partition(arr,lo,hi):
    #print("partitioning: "+str(lo)+" to "+str(hi))
    if hi <= lo:
        return
    lt = lo
    gt = hi
    v = arr[lo] #pivot
    i = lo
    while i <= gt:
        if arr[i] == v:
            i = i + 1
        elif arr[i] < v:
            swap(arr,lt,i)
            lt = lt + 1
            i = i + 1
        else:
            swap(arr,i,gt)
            gt = gt - 1
        pass
    pass
    partition(arr,lo,lt-1)
    partition(arr,gt+1,hi)
pass

def Qsort(arr):
    partition(arr,0,len(arr)-1)
    return arr
pass


n = int(input())
i = 0
arr = []
while i < n:
    arr.append(int(input()))
    i=i+1
pass
print(Qsort(arr))