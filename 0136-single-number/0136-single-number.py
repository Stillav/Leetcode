class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count_dict = dict()
        for i in nums:
            if i in count_dict:
                count_dict[i] +=1
            else:
                count_dict[i] = 1
                
        for i in count_dict:
            if count_dict[i] == 1:
                return i
            