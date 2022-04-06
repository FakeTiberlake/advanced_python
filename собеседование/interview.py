class Stack(list):

    def __init__(self):
        super().__init__(self)

    def size(self):
        return len(self)

    def is_empty(self):
        return self.size() < 1

    def push(self, item):
        self.append(item)

    def pop(self):
        super().pop(self.size() - 1)

    def peek(self):
        return self[self.size() - 1]


def check_string(string):
    opening = ['(', '{', '[']
    closing = [')', '}', ']']
    open_par = Stack()

    if len(string) % 2 > 0:
        return 'Несбалансированно'

    for i, char in enumerate(string):
        if char in opening:
            open_par.push(char)
        elif char in closing:
            if open_par.is_empty():
                return 'Несбалансированно'
            elif opening.index(open_par.peek()) != closing.index(char):
                return 'Несбалансированно'
            else:
                open_par.pop()
                if open_par.is_empty() and i == len(string)-1:
                    return 'Сбалансированно'


if __name__ == '__main__':
    print(check_string(input('Введите строку')))