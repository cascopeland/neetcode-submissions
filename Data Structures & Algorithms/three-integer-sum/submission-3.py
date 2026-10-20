class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # [-4, -1, -1, 0, 1, 2]
        nums.sort()
        sum_list = []
        i = 0
        while i < len(nums)-1:
            l, r = i + 1, len(nums) - 1
            # THIS PART WAS GIVING ME ISSUES
            # But ITS EASy AND I THINK THAT IN INTERVIEW IT WOULD BE FINE
            if i > 0 and nums[i-1] == nums[i]:
                i+=1
                continue
            while l < r:
                target_diff = nums[i] + nums[l] + nums[r]
                if target_diff > 0:
                    r -= 1
                elif target_diff < 0:
                    l += 1
                else: #target_diff == 0:
                    sum_list.append([nums[i], nums[l], nums[r]])
                    l+=1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
                
            i+=1
        return sum_list