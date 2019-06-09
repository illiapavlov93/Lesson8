class Parentheses:
    def __init__(self, line, verification=False):
        self.line = line
        self.verification = verification

    @classmethod
    def from_input(cls):
        return cls(input('Введите строку скобочек '))

    def verify(self, brackets='{}[]()<>'):
        for i in self.line:
            if i not in brackets:
                self.verification = False
                return self.verification
            else:
                self.verification = True
        return self.verification

    def is_balanced(self, brackets='{}[]()<>'):
        opening, closing = brackets[::2], brackets[1::2]
        stack = []
        self.verify()
        if self.verification:
            for i in self.line:
                if i in opening:
                    stack.append(opening.index(i))
                elif i in closing:
                    if stack and stack[-1] == closing.index(i):
                        stack.pop()
                    else:
                        return 'Строка не являеться правильной скобочной последовательностью'
            if stack:
                return 'Строка не являеться правильной скобочной последовательностью'
            else:
                return 'Строка являеться правильной скобочной последовательностью'
        else:
            return 'Строка не состоит только из скобок'


c = Parentheses.from_input()
print(c.verify())
print(c.is_balanced())
