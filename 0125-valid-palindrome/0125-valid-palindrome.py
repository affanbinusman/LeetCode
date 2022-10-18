class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        
        temp= ""
        
        for i in s:
            if i.isalnum():
                temp = temp + i.lower()
        return temp == temp[::-1]
        
        
#         # left pointer = l
#         # right pointer = r
        
#         while l<r:
#             while l<r and not self.alpha_numeric_check(s[l]):
#                 l = l+1
#             while r>l and not self.alpha_numeric_check(s[r]):
#                 r = r-1
        
#             if s[l].lower() != s[r].lower():
#                 return False
#             l = l+1
#             r = r-1
#         return True
            
        
#     def alpha_numeric_check(self, word):
#         return (ord("A") <= ord(word) <= ord("Z") or
#                 ord("a") <= ord(word) <= ord("z") or
#                 ord("0") <= ord(word) <= ord("9"))