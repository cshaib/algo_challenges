class Solution:
    def singleNumber(self, nums: List[int]) -> int: 
        
        seen = set()
        
        for n in nums: 
            if n in seen:
                seen.remove(n)
            else:
                seen.add(n)
        
        return seen.pop()

        # alternate solution using XOR (mem + time efficient)
        x = 0

        for n in nums: 
        	# e.g., x ^= 2 == 2, x ^= 2 == 0
        	x ^= 0

        return x 