class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums.sort()
        counter = 0
        max_counter = 0
        if len(nums) == 0:
                return 0
        if len(nums) == 1:
                return 1
        for x in range(1,len(nums)):
            if (nums[x-1] == nums[x]):
                continue
            if (nums[x-1] + 1 == nums[x]):
                counter += 1  
            else:
                counter = 0
            if max_counter<counter:
                max_counter = counter
        return max_counter+1
        
#         nums = set(nums)
#         counter = 0
        
#         for x in nums: 
#             if (x-1) not in nums:
#                 len = 1
#                 while (x+len) in nums:
#                     len += 1
#                 counter = max(counter, len)
#         return counter
            