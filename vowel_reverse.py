class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        recomb_str = []

        ptr1 = 0
        ptr2 = 0
        s_rev = s[::-1]
        
        while ptr1 < len(s):
            if s[ptr1] not in vowels:
                recomb_str.append(s[ptr1])
                ptr1 += 1
            else:
                if s_rev[ptr2] not in vowels:
                    ptr2 += 1
                else:
                    recomb_str.append(s_rev[ptr2])
                    ptr2 += 1
                    ptr1 += 1

        return ''.join(recomb_str)
            