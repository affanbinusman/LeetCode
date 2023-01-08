class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        
        def bktrack(openn, closen):
            if n == openn == closen:
                res.append("".join(stack))
                return
            
            if openn < n:
                stack.append("(")
                bktrack(openn +1, closen)
                stack.pop()
                
            if closen < openn:
                stack.append(")")
                bktrack(openn, closen + 1)
                stack.pop()
                
        bktrack(0,0)
        return res