def evalRPN(tokens: list[str]) -> int:
    stack = []
    operators = set(['+', '-', '*', '/'])
    for token in tokens:
        if token not in operators:
            stack.append(token)
        else:
            x = int(stack.pop())
            y = int(stack.pop())
            if token == '+':
                stack.append(y + x)

            elif token == '-':
                stack.append(y - x)
            
            elif token == '/':
                stack.append(int(y / x))

            elif token == '*':
                stack.append(y * x) 

    if stack:
        return int(stack[0])


def main():
    rpn_tokens = ["10", "12"]
    print(evalRPN(rpn_tokens))

main()



