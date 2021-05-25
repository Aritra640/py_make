import sys

def get():
    return sys.stdin.readline()

n,x = map(int,get().split())
p = list(map(int,get().split()))

p.sort()

gondolas = 0
pointer1,pointer2 =0,n-1

while pointer1<=pointer2 :
    
    if p[pointer1]+p[pointer2]<=x :
        pointer1 += 1 
    
    pointer2 -= 1
    gondolas += 1

sys.stdout.write(str(gondolas)+"\n")        