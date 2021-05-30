import sys

def getinput():
    return sys.stdin.readline()

n = int(getinput())
arr = list(map(int,getinput().split()))
m = max(arr)
count = [0 for i in range(m+1)]


for i in range(n):
    count[arr[i]] += 1
for i in range(1,m+1):
    count[i] += count[i-1]
ans = [0 for i in range(n)]
for i in range(n):
    count[arr[i]] -= 1
    ans[count[arr[i]]] = arr[i] 
sys.stdout.write(" ".join(map(str,ans))+"\n")    
          