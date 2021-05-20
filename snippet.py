import sys
import os

#fast i/o in python 3
# for normal input :
def getintegers():
    return map(int, sys.stdin.readline().strip().split())

def getlist():
    return list(map(int, sys.stdin.readline().strip().split()))

def get():
    return sys.stdin.readline().strip()

# only for online judges :
input = io.BytesIO(os.read(0, \ os.fstat(0).st_size)).readline #sometimes it will not woek

#to take string input do this :
s = input().decode()

n = 5
sys.stdout.write(str(n)+"\n") # printing integers

# for printing  string 
s = "Hello World!"
sys.stdout.write(s)

#for printing a list of integers :
arr = [1,2,3,4,5]
sys.stdout.write(
    " ".join(map(str,arr))+"\n"
)
