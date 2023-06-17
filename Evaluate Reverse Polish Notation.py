def evalRPN(tokens):
    import operator
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }
    stack = []
    for char in tokens:
        if char.isdigit():
            stack.append(int(char))
        elif char.startswith('-') and len(char) > 1:
            stack.append(int(char))
        else:
            temp = int(ops[char](stack[-2], stack[-1]))
            stack.pop()
            stack.pop()
            stack.append(temp)

            temp = 0
    return stack [0]
print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))