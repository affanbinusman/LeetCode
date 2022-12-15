class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hmap1 = {}
        hmap2 = {}
        
        if len(s1) > len(s2): return False
        
        for i in range(len(s1)):
            hmap1[s1[i]] = hmap1.get(s1[i], 0) + 1
            hmap2[s2[i]] = hmap2.get(s2[i], 0) + 1
        
        index = ord("a")
        matches = 0
        for i in range(26):
            if hmap1.get(chr(index + i), 0) == hmap2.get(chr(index + i), 0):
                matches += 1
        l = 0
        for r in range(len(s1), len(s2)):
            # print(r, s2[r])
            # print(1, hmap1, hmap2, matches)
            if matches == 26:
                # print(11, hmap1, hmap2, matches)
                return True
            
            hmap2[s2[r]] = hmap2.get(s2[r], 0) + 1
            if hmap1.get(s2[r], 0) == hmap2[s2[r]]:
                matches += 1
            elif hmap1.get(s2[r], 0) + 1 == hmap2[s2[r]]: 
                matches -= 1
            # print(2, hmap1, hmap2, matches)
            
            hmap2[s2[l]] = hmap2[s2[l]] - 1
            if hmap1.get(s2[l], 0) == hmap2[s2[l]]:
                matches += 1
            elif hmap1.get(s2[l], 0) - 1 == hmap2[s2[l]]: 
                matches -= 1
            l += 1
            # print(3, hmap1, hmap2, matches)
            
        if matches==26: return True 
        else: return False      