class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit
        pass

    def isEmpty(self):
        return len(self.items) == 0
        pass

    def push(self, item):
        if len(self.items) < self.limit:
            return self.items.append(item)
        # else: 
        #     raise ValueError("Limit Stack size reached.")   
        #     return  
        # return self.items       
        pass

    def pop(self):
        if len(self.items) == 0:
            return None
        else:    
            return self.items.pop()
        pass

    def peek(self):
        return self.items[-1]
        pass
    
    def size(self):
        return len(self.items)
        pass

    def full(self):
        return len(self.items) >= self.limit
        pass

    def search(self, target):
        if target in self.items:
            return(len(self.items) - (self.items.index(target) + 1))
        else:
            return -1    
        pass





# list_ = [1,2,3,4,5,6]

# print(len(list_) - (list_.index(6)+1))

# (list_.append(7))

# print(list_)
# list_.pop()

# print(list_)

stack = Stack([1,2,3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6], 15)

# print(stack.isEmpty())
print(stack.full())
print(stack.isEmpty())
# print(stack.full())
# print(stack.full())
# print(stack.pop())
# print(stack.push(15))
# print(stack.push(16))
# print(stack.search(9))
# print(stack.push(17))

     
