class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == '+':
                v = stack.pop() + stack.pop()
                stack.append(v)
            elif t == '*':
                v = stack.pop() * stack.pop()
                stack.append(v)
            elif t == '-':
                o1 = stack.pop()
                o2 = stack.pop()
                stack.append(o2 - o1)
            elif t == '/':
                o1 = stack.pop()
                o2 = stack.pop()
                stack.append(int(o2/o1))
            else:
                stack.append(int(t))
        return stack.pop()