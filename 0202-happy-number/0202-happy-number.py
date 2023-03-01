class Solution:
    def isHappy(self, n: int) -> bool:
        store = set()
        
        while n not in store:
            store.add(n)
            n = self.sos(n)
            if n == 1:
                return True
        
        return False 
    
    def sos(self, n):
        sumsos = 0
        
        while n != 0:
            digit = n%10
            digit = digit * digit
            sumsos += digit
            n = n//10
        return sumsos
            