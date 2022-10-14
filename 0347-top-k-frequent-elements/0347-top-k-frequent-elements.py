class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        output = []

        for x in range(0,len(nums)):
            dict1[nums[x]] = 1 + dict1.get(nums[x],0)
        
        dict1 = sorted(dict1.items(), key=lambda x: x[1], reverse = True)
        
        y = 0
        for keys, _ in dict1:
            output.append(keys)
            y += 1
            if y ==k:
                return output