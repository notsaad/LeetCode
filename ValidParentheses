class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        if len(s) < 2:
            return False

        for char in s:
            if char == "(" or char == "{" or char == "[": # add open bracket to stack
                stack.append(char)
            elif len(stack) == 0:
                return False
            else: # determine what type of closing bracket it is
                if char == ")" and stack.pop() == "(":
                    continue
                elif char == "]" and stack.pop() == "[":
                    continue
                elif char == "}" and stack.pop() == "{":
                    continue
                else:
                    return False

        return True if len(stack) == 0 else False
