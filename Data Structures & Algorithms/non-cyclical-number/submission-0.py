class Solution:
    def isHappy(self, n: int) -> bool:
        
        for _ in range(100):

            total = 0

            if n == 1:
                return True

            while n > 0:
                digit = n % 10
                total += digit * digit
                n //= 10
            
            n = total

        return False