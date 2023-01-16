class Solution:
    rep = [i for i in range(26)]
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        
        if x == y:
            return 
        
        if x > y:
            self.rep[x] = y
        else:
            self.rep[y] = x
            
    def find(self, x):
        if self.rep[x] == x:
            return x
        
        self.rep[x] = self.find(self.rep[x])
        return self.rep[x]
    
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        res = ""
        for i in range(26):
            self.rep[i] = i
        
        a = ord("a")
        for i in range(len(s1)):
            self.union(ord(s1[i]) - a, ord(s2[i]) - a)
            
        for c in baseStr:
            res += chr(self.find(ord(c)-a) + a)
            
        return res
            
        