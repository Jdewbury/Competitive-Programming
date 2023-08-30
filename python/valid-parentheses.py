class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = dict(("()", "{}", "[]"))

        for i in s:
            if i in pairs:
                stack.append(i)
            elif len(stack) == 0 or i != pairs[stack.pop()]:
                return False
        return len(stack) == 0