class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1:
            return [[1]]
        
        result = [[1]]
        
        for i in range(2, numRows+1):
            if i != 2:
                temp = [0] * (i - 2)
                temp.insert(0, 1)
                temp.append(1)
            else: 
                temp = [1,1]
                
            result.append(temp)

        for i, row in enumerate(result):
            for j, col in enumerate(row):
                if col == 0:
                    result[i][j] = result[i-1][j-1] + result[i-1][j]
                    
        return result