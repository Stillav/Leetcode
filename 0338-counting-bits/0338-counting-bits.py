class Solution:
    def countBits(self, n: int) -> List[int]:
        answer = list()
        for num in range(n + 1):
            num_bit = bin(num)[2:]
            answer.append(num_bit.count('1'))
            
        return answer 