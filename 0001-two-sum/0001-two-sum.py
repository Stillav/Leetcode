class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos_dict = {num: i for i, num in enumerate(nums)}
        
        for i, num in enumerate(nums):
            if target - num in nums and i != pos_dict[target - num]:
                return [i, pos_dict[target - num]]