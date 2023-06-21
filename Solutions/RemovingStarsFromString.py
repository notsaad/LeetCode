class Solution:
    def removeStars(self, s: str) -> str:

        stack = []

        for x in s:
            if x == "*":
                stack.pop()
            else:
                stack.append(x)
        
        res = ""

        for c in stack:
            res += c

        return res
