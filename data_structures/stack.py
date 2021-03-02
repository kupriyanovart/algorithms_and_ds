class Stack():
    _s = []
    
    def push(self, x):
        self._s.append(x)
        
    def pop(self):
        if self._s:
            return self._s.pop()
        print('Стек пуст!')
    
    def size(self):
        return len(self._s)
        
    def is_empty(self):
        return not bool(len(self._s))
        
    def top(self):
        if self._s:
            return self._s[-1]
        print('Стек пуст!')
        

def is_bracket_sequence_correct(s: str):
    '''
    Функция проверки корректности скобочной последовательности, состоящей из круглых и квадратных скобок ()[]
    Корректные скобочные последовательности:
    A = ""
    B = (A)
    C = AB
    B = [A]
    '''
    stack = Stack()
    for br in s:
        if br not in '()[]':
            continue
        if br in '([':
            stack.push(br)
        else:
            if stack.is_empty():
                return False
            left = stack.pop()
            right = ')' if left == '(' else ']'
            if br != right:
                return False
    return stack.is_empty()
    
print(is_bracket_sequence_correct('()[][[[([])]]]'))


def reverse_polish_notation(s: list):
    stack = Stack()
    operations = '+', '-', '*', '/'
    for c in s:
        if type(c) == int or type(c) == float:
            stack.push(c)
        else:
            if c in operations and stack.size() > 1:
                right = stack.pop()
                left = stack.pop()
                if c == '+':
                    res = left + right
                elif c == '-':
                    res = left - right
                elif c == '*':
                    res = left * right
                else:
                    res = left / right
                stack.push(res)
            else:
                print('Недопустимая операция')

    if stack.size() != 1:
        print('Недопустимые входные данные')
        return
    return stack.pop()

print(reverse_polish_notation([1, 2, 4, '+','-']))

