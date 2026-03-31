class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for symbol in s:
            if symbol == "(" or symbol == "[" or symbol == "{":
                stack.append(symbol)
                continue
            if len(stack) == 0:
                return False
            if symbol == ")":
                if stack.pop() != "(":
                    return False
            if symbol == "]":
                if stack.pop() != "[":
                    return False
            if symbol == "}":
                if stack.pop() != "{":
                    return False
        if len(stack) != 0:
            return False
        return True