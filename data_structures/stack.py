class Stack():
    s = []
    
    def push(self, x):
        self.s.append(x)
        
    def pop(self):
        if self.s:
            return self.s.pop()
        print('Стек пуст!')
    
    def size(self):
        return len(self.s)
    
    def top(self):
        if self.s:
            return self.s[-1]
        print('Стек пуст!')
        

