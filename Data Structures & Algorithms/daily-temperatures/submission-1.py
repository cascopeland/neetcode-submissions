class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        # 30, 38
        # 0, 1

        # get index and temperature for each day
        for i, t in enumerate(temperatures):
            # while stack exists and temperature greater than top of stack, then we can populate result list

            
            while stack and t > stack[-1][1]:
                # we get the top stack value (smaller)
                iStack, tStack = stack.pop()
                # then we populate with current index - smaller temp index
                result[iStack] = i - iStack
            # if not smaller or stack does not exist yet
            # then we need to add to stack
            stack.append((i, t))
        return result
