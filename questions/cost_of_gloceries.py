# Cost of gloceries
# In this program i'm little bit stuck to understand the input pattern
class Solution:
    def compute(self, n, x, a, b):
        # write your code here 
        cost=0
        for i in range(n):
            if a[i] >= x:
               cost+=b[i]
        return cost
