class Solution:
    def defangIPaddr(self, address: str) -> str:
        s = ""

        for c in address:
            if "." == c:
                s = s + "["
                s = s + "."
                s = s + "]"
            else:
                s = s + c
        return s
