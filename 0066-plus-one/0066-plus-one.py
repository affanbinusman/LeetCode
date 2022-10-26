class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        if digits[len(digits)-1] != 9:
                digits[len(digits)-1] = digits[len(digits)-1] + 1
                return digits
        else:
            len1 = len(digits)-1
            carry = 0
            
            for i in range(len1, -1, -1):
                if digits[i] == 9 and carry == 0 and i != len1:
                    return digits
                if digits[i] == 9:
                    digits[i] = 0 
                    carry = 1
                elif digits[i] != 9:
                    digits[i] = digits[i] + carry
                    carry = 0
                
            
            if digits[0] == 0 and carry==1:
                digits.insert(0,1)
                
            
            
            
            return digits