class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l = 0
        r = len(numbers) - 1 
        
        while (numbers[l] + numbers[r] != target):
            if (numbers[l] + numbers[r] > target):
                r -= 1
                print(r)
            elif (numbers[l] + numbers[r] < target):
                l += 1
                print(l)
        
        if (numbers[l] + numbers[r] == target):
                return [l+1,r+1]
            