class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = list()
        nums.sort()
        
        for i, val in enumerate(nums):
            if i > 0 and val == nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1
            while l < r:
                three_sum = val + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([val, nums[l], nums[r]])
                    l += 1
                    while (nums[l] == nums[l-1]) and l < r:
                        l += 1
        return res
        
        
#         for i in range(len(nums)):
#             temp = nums[i]
#             l = i + 1
#             r = len(nums) - 1
#             while l < r:
#                 print(nums[i], nums[l], nums[r])
#                 if nums[l] + nums[r] == -temp:
#                     res2 = [temp,nums[l],nums[r]]
#                     res2.sort()
#                     if res2 in res:
#                         break
#                     res.append(res2)
#                     l += 1
#                 elif nums[l] + nums[r] > -temp:
#                     r -= 1
#                 else:
#                     l += 1
#         return res
                    
                    