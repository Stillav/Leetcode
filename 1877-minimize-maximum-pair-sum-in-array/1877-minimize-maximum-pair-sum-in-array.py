class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max_sum = float('-inf')
        
        for i in range(len(nums) // 2):
            if nums[i] + nums[-(i+1)] > max_sum:
                max_sum = nums[i] + nums[-(i+1)]
                
        return max_sum