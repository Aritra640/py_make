
def merge(arr,l,r,m):
    
    n1 = m - l + 1
    n2 = r - m
    a = list()
    b = list()
    for i in range(0,n1):
        a.append(arr[l+i])
    for i in range(0,n2):
        b.append(arr[m+i+1])
    p1 = 0
    p2 = 0
    t = l
    while p1<n1 and p2<n2 :
        if a[p1]<b[p2] :
            arr[t]=a[p1]
            t = t + 1
            p1 = p1 + 1
        else :
            arr[t] = b[p2]
            t = t + 1
            p2 = p2 + 1
    while t<=r and p1<n1 :
        arr[t]=a[p1]
        p1 = p1 + 1
        t = t + 1
    while t<=r and p2<n2 :
        arr[t]=b[p2]
        t = t + 1
        p2 = p2 + 1                  

def mergesort(arr,l,r):
    
    if l<r :
        mergesort(arr,l,((l+r)/2))
        mergesort(arr,(((l+r)/2)+1),r)
        merge(arr,l,r,((l+r)/2))

def main():
    n = int(input("Enter the number of terms  : "))
    print("Enter your list here : ")
    arr = list([int(i) for i in input().split()])
    mergesort(arr,0,n-1)
    print(arr)

# driver code 
if __name__ == "__main__" :
    main()
