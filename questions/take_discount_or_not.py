# Take discount or not (CodeChef array question)
# This approach according to me
class Solution:
    def check_coupon(self, n, x, y, prices):
        # write your code here
        cost=0
        c_cost=0
        for i in prices:
           cost+=i
           c_cost=c_cost+max(0,i-y)
        if c_cost+x < cost:
           return "COUPON"
        return "NO COUPON"

t=int(input())
s=Solution()

for _ in range(t):
    n,x,y=map(int,input().split())
    prices=list(map(int,input().split()))
    print(s.check_coupon(n,x,y,prices))
