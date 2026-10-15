class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        combos = {"}" : "{", "]":"[", ")":"("}

        for c in s:
            if c in combos:
                if len(stack) != 0 and stack[-1] == combos[c]:
                    stack.pop()
                else:
                     return False
            if c not in combos:
                stack.append(c)
        if len(stack) != 0:
            return False 
        return True