class Solution:
    def checkValidString(self, s: str) -> bool:
        if s[0] == ")" or s[-1] == "(":
            return False

        stack_left, stack_star = [], []
        for i in range(len(s)):
            if s[i] == "(":
                stack_left.append(i)
            elif s[i] == ")":
                if stack_left:
                    stack_left.pop()
                elif stack_star:
                    stack_star.pop()
                else:
                    return False
            else:
                stack_star.append(i)

        while stack_left and stack_star:
            sl = stack_left.pop()
            ss = stack_star.pop()
            while sl > ss:
                if not stack_star:
                    return False
                ss = stack_star.pop()

        return not stack_left