class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t: return s
        if len(s) < len(t): return ""
        if t == "": return ""
        
        res = [-1,-1]
        reslen = float("infinity")
        hmapt, hmapw = {}, {}
        have, need = 0, len(t)
        
        for i in range(len(t)):
            hmapt[t[i]] = hmapt.get(t[i], 0) + 1
        
        l = 0
        for r, val in enumerate(s):
            hmapw[val] = 1 + hmapw.get(val, 0)
            
            if val in t and hmapw[val] <= hmapt[val]:
                have += 1
            # print(hmapt, hmapw, have, need)
            
            while have == need:
                # print("comes here")
                if (r - l + 1) < reslen:
                    res = [l, r+1]
                    reslen = r - l + 1
                hmapw[s[l]] -= 1
                if s[l] in hmapt and hmapw[s[l]] < hmapt[s[l]]:
                    have -= 1
                l += 1

        if reslen != float("infinity"): 
            return s[res[0]: res[1]] 
        else: 
            return ""

        