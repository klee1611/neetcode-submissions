class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == '+':
                stack.append(stack.pop() + stack.pop())
            elif t == '*':
                stack.append(stack.pop() * stack.pop())
            elif t == '-':
                op = stack.pop()
                stack.append(stack.pop() - op)
            elif t == '/':
                op = stack.pop()
                stack.append(int(stack.pop() / op))
            else:
                stack.append(int(t))
        return stack.pop() 