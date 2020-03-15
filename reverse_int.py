class Solution:
    def reverse(self, x: int) -> int:
        try:
            rev = int(str(x)[::-1])
        except ValueError: 
            x = str(x)[::-1]
            rev = -1 * int(x[:-1])
        
        # check for overflow
        if(abs(rev) > (2 ** 31 - 1)) or (abs(rev) > (1 << 31) - 1):
            return 0

        return rev