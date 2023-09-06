# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:

        bounds  = (-2**31 , 2**31 - 1)
        number = 0

        signal = 1
        if x < 0:
            signal = -1
            x *= -1

        for i,c in enumerate(str(x)):

            if signal * int(c) * 10**i + number >= bounds[0] and signal * int(c) * 10**i + number <= bounds[1]:
                number += signal * int(c) * 10**i

            else:
                return 0

        return number