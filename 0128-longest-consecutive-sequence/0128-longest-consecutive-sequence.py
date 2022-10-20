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
            