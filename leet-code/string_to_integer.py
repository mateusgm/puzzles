# https://leetcode.com/problems/string-to-integer-atoi/

import re

class Solution:
    def myAtoi(self, s: str) -> int:

        bounds = (-2**31, 2**31 - 1)

        sign   = 0
        number = []

        for c in s:
            if c in " \t\n" and len(number) == 0 and sign == 0:
                next
            elif c in '-' and len(number) == 0 and sign == 0:
                sign = -1
            elif c in '+' and len(number) == 0 and sign == 0:
                sign = 1
            elif c in "0123456789":
                number.append(int(c))
            else:
                break

        if sign == 0:
            sign = 1

        total = 0
        for i,n in enumerate(number[::-1]):
            total += sign * n * 10**i

        return max(bounds[0], min(total, bounds[1]))
