class Solution:
    def countBits(self, n: int) -> List[int]:

        ans = []

        for i in range(n + 1):

            num = i
            count = 0

            while num:
                count += num & 1
                num >>= 1
            
            ans.append(count)
        
        return ans