class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        num_dict = dict()
        result_dict = dict() 
        for num in arr:
            if num_dict.get(num):
                num_dict[num] += 1
            else:
                num_dict[num] = 1 
                
        for key, value in num_dict.items():
            if result_dict.get(value):
                return False 
            result_dict[value] = key 
        
        return True