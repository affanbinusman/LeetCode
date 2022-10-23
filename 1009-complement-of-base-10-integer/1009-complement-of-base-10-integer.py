class Solution:
    def bitwiseComplement(self, n: int) -> int:
        n_b = str(bin(n))
        nn  = ""
        for i in n_b[2:]:
            # print(i)
            if i == "0":
                nn += "1"
            else:
                nn += "0"
        
        return int(nn,2)