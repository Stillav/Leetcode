class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # return list(itertools.permutations(nums,len(nums)))
        result = list()
        temp = list()
        def dfs(elements):
            if len(temp) == len(nums):
                result.append(temp[:])
                return 
            
            new_elements = elements[:]
            for element in elements:
                new_elements.remove(element)
                temp.append(element)
                
                dfs(new_elements)
                new_elements.append(element)
                temp.remove(element)
                
        dfs(nums)
        
        return result