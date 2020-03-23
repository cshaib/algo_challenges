class Solution:
    def romanToInt(self, s: str) -> int:
        
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000   
        }
        
        n = 0
        
        # tricky off by one when looping 
        for i, v in enumerate(s):
            if i + 1 < len(s) and roman_dict[v] < roman_dict[s[i+1]]:
                n -= roman_dict[v]
            else:
                n += roman_dict[v]
        return n
                