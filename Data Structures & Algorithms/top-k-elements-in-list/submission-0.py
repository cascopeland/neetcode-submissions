class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # okay, the game plan is to drop the top k elements from the list into a list
        # so, we will iterate through nums and populate hash map key value pair
        k_elements = []
        nums_dict = {}
        for i in range(len(nums)):
            nums_dict[nums[i]] = nums_dict.get(nums[i], 0) + 1
        for ks in range(k):
            max_key = max(nums_dict, key=nums_dict.get)
            k_elements.append(max_key)
            nums_dict.pop(max_key, 0)
        return k_elements