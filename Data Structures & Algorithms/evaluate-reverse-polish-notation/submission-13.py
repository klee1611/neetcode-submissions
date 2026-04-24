class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "-":
                op = stack.pop()
                stack.append(stack.pop() - op)
            elif token == "/":
                op2, op1 = stack.pop(), stack.pop()
                stack.append(int(op1 / op2))
            else:
                stack.append(int(token))

        return stack.pop()