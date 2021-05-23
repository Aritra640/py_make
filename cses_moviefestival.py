import sys
def getinput():
    return sys.stdin.readline()
n = int(getinput())
arr = [[int(i) for  i in getinput().split()] for _ in range(n)]
arr.sort(key = lambda x:x[1])
end = arr[0][1]
c = 1
for i in range(1,n):
    if arr[i][0] >= end :
        end = arr[i][1]
        c += 1 
sys.stdout.write(str(c)+"\n")        