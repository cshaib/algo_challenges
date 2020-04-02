class Solution:
    def isHappy(self, n: int) -> bool:
        def _sq_digits(n):
            return sum(map(lambda x:int(x)**2, str(n)))
    
        if n == 1:
            return True
        elif n == 4: # https://en.wikipedia.org/wiki/Happy_number#10-happy_numbers
            return False
        else: 
            total = _sq_digits(n)
            return self.isHappy(total)
        
# alternate solution using tortoise and hare -- e.g., if happy number cycle not known

#         def next_num(num):
#             return sum(map(lambda x:int(x)**2, str(num)))
        
#         slow, fast = n, next_num(n)
        
#         while slow != fast and fast != 1:
#             slow = next_num(slow)
#             fast = next_num(next_num(fast))
            
#         return fast == 1 or not slow == fast