class Solution:
    def majorityElement(self, nums: List[int]) -> int:
#         result = dict()
#         if len(nums) == 1:
#             return nums[0]
        
#         else:
#             for i in nums:
#                 if str(i) in result:
#                     result[str(i)] += 1
#                     if result[str(i)] > len(nums)//2:
#                         return i
#                 else:
#                     result[str(i)] = 1
        return list(Counter(nums).most_common(1))[0][0]
                 

        
                
            