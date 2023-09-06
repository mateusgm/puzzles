# https://leetcode.com/problems/zigzag-conversion/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        
        rows = ["" for i in range(numRows) ]
        current = 0
        trend   = -1
        
        for i,c in enumerate(s):        
            rows[current] += c
            
            if current == numRows-1 or current == 0:
                trend *= -1
            if current + trend >= 0 and current + trend < numRows:
                current += trend
        
        return "".join(rows)