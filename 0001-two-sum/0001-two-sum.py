class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = list()
        for i, value in enumerate(nums):
            if target - value in nums and nums.index(target - value) != i:
                answer = [i, nums.index(target - value)]
                
                return answer 