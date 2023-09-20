class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        num1_dict = {key: 1 for key in nums1}
        num2_dict = {key: 1 for key in nums2}
        
        num1_list, num2_list = list(), list()
        
        for num in nums1:
            if not num2_dict.get(num):
                num1_list.append(num)
                
        for num in nums2:
            if not num1_dict.get(num):
                num2_list.append(num)
                
        return [list(set(num1_list)), list(set(num2_list))]