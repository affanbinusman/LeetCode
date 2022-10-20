class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = set(nums)
        counter = 0
        
        for x in nums: 
            if (x-1) not in nums:
                len = 1
                while (x+len) in nums:
                    len += 1
                counter = max(counter, len)
        return counter
            