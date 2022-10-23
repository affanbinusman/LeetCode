class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dict1 = {}
        
        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in dict1:
                return [i, dict1[dif]]
            dict1[nums[i]] = i
                
                        
