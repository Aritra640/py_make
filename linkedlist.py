class node :
    
    def __init__(self,data = None):
        
        self.data = data
        self.next = None

class linked_list :
    
    def __init__(self):
        
        self.head = node()
        
    def append(self,val) :
        
        new_node = node(val)
        cur = self.head 
        while cur.next != None :
            cur = cur.next
        cur.next = new_node 
    
    def length(self):
        
        count = 0
        cur = self.head 
        while cur.next != None :
            
               count += 1 
               cur = cur.next 
        
        return count  
    
    def get(self):
        
        cur = self.head
        arr = list()
        while cur.next != None :
            
            cur = cur.next 
            arr.append(cur.data)
            
        return arr    
            
            
            


if __name__ == '__main__':
    
    obj = linked_list()
    n = int(input("Enter number of element : "))
    for i in range(n):
        
        temp = int(input("Enter number :"))
        obj.append(temp)
    
    ele = obj.get()
    print(ele)