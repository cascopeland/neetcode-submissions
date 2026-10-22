class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        # 30, 38
        # 0, 1
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                iStack, tStack = stack.pop()
                result[iStack] = i - iStack
            stack.append((i, t))
        return result
