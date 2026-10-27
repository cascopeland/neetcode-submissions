class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, i_l = 0, 0
        i_r = len(heights)- 1
        r = heights[i_r]
        container = 0
        while (i_r > i_l):
            l = heights[i_l]
            r = heights[i_r]
            new_container = (i_r - i_l) * (min(l, r))
            container = max(container, new_container)
            if l < r:
                i_l +=1
            else:
                i_r -= 1
        return container

