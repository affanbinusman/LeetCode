class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        res = list()
        q = collections.deque()
        l = 0
        r = 0
        
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            
            if q[0] < l:
                q.popleft()
            
            if (r+1) >= k:
                res.append(nums[q[0]])
                l += 1
            r += 1
            
        return res
                
        
        
        
        
        
        # second approach
#         l = 0
#         length = len(nums)
#         r = k
#         res = list()
        
#         while r-l == k:
            
#             max1 = max(nums[l:r])
#             index1 = nums.index(max1)
#             # print(1, l,r,max1) 
            
#             if index1%2 == 0: 
#                 index2 = index1//2
#             else:
#                 index2 = index1//2 + 1
            
#             while l +1 < index1 - index2 :
#                 # print(4)
#                 res.append(max1)
#                 l += 1
                
#                 if r + 1 <= length:
#                     r += 1
#                     # print(2, l,r,max1)
#                     continue
#                 else: continue
            
#             res.append(max1)
#             l += 1
#             if r + 1 <= length:
#                 r += 1
#                 continue
#             else: continue
        
#         return res
     #first approach   
        #         res = list()
#         length = len(nums)
#         r = k
        
#         for l in range(0, len(nums)-k+1):
#             # print(l, r, res)
#             res.append(max(nums[l:r]))
# #             if r + 1 > length:
                
# #                 break
# #             else:
#             r += 1
#         return res