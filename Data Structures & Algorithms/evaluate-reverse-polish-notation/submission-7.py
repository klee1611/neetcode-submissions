class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        cal_stack = [int(tokens[0])]
        for i in range(1, len(tokens)):
            t = tokens[i]
            if not (t == '+' or t == '-' or t == '*' or t == '/'):
                cal_stack.append(int(t))
                continue
            if t == '+':
                r = cal_stack.pop() + cal_stack.pop()
                cal_stack.append(r)
            if t == '-':
                o1 = cal_stack.pop()
                o2 = cal_stack.pop()
                cal_stack.append(o2-o1)
            if t == '*':
                r = cal_stack.pop() * cal_stack.pop()
                cal_stack.append(r)
            if t == '/':
                o1 = cal_stack.pop()
                o2 = cal_stack.pop()
                cal_stack.append(int(o2 / o1))
        return cal_stack.pop()