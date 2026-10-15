class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # nums is sorted in order
        # Search for target within nums, if exists, return index
        ## else: return -1

        low = 0
        high = len(nums) - 1
        while low <= high:
            # set midpoint to be 
            # ex: (l = 1, r = 4, midpoint = 2)
            midpoint = low + ((high - low) // 2)
            if nums[midpoint] < target:
                low = midpoint + 1
            elif nums[midpoint] > target:
                high = midpoint - 1
            else: 
                return midpoint
        return -1




