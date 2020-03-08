class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        ptr1 = 0
        ptr2 = len(s)-1
        
        s = [char for char in s]
        
        while ptr1 < ptr2:
            if s[ptr1] not in vowels:
                ptr1 += 1
            else:
                if s[ptr2] not in vowels:
                    ptr2 -= 1
                else:
                    tmp = s[ptr1]
                    s[ptr1] = s[ptr2]
                    s[ptr2] = tmp
                    ptr2 -= 1
                    ptr1 += 1

        return ''.join(s)