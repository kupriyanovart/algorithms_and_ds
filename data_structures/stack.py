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
        
st = Stack()
print(st.size())
st.push(2)
st.push(3)
print(st.size())
print(st.top())
print(st.pop())
print(st.size())
