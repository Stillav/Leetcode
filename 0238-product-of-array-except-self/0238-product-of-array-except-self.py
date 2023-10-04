class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre_mul, pos_mul = 1, 1 
        result = [0] * n 
        
        for i in range(n):
            result[i] = pre_mul
            pre_mul *= nums[i]
        
        for i in range(n-1, -1, -1):
            result[i] *= pos_mul
            pos_mul *= nums[i]
           
        return result
        
        