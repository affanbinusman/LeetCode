class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)
        longest = 0

        for n in nums:
            # check if its the start of a sequence
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
    
#         nums = set(nums)
#         counter = 0
        
#         for x in nums: 
#             if (x-1) not in nums:
#                 len = 1
#                 while (x+len) in nums:
#                     len += 1
#                 counter = max(counter, len)
#         return counter
            