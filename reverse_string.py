class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for idx,char in enumerate(s[:int(len(s)/2)]):
            tmp = char
            s[idx] = s[-idx-1]
            s[-idx-1] = tmp
        return
            
            