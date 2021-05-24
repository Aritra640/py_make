n = int(input("Enter number of elements : "))
print("Enter your list here")
arr = [int(i) for i in input().split()]
x = int(input("Enter your number to be found"))

arr.sort()

l,u,p = 0,n-1,-1

while l<=u :
    
    m = (l+u)//2
    if arr[m] == x :
        p = m 
        break
    else :
        if arr[m]>x :
            u = m - 1
        elif arr[m]<x :
            l = m + 1

ans = str(x)
if p == -1 :
    ans = ans+ " is not fount!"
else  :
    ans = ans + " is found at index "+str(p)
print(ans)
    
                    