# Ques: Single number in multiple numbers (find unique number)
''' Input:
3
1
10
5
9 1 9 2 1
5
7 3 5 3 7
'''

class Solution:
    def singleNumber(self, nums):
        # write your code here
        
        for i in range(len(nums)):
            count_num=nums.count(nums[i])
            if count_num==1:
                return nums[i]
''' Output
10
2
5'''
''' New method 
class Solution:
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result ^= num  # XOR accumulates the unique number
        return result

Explanation:
👉 Important properties:

a ^ a = 0
a ^ 0 = a
XOR commutative & associative hai
(order matter nahi karta)
Instead of binary:
Same number cancel ho jata hai → a ^ a = 0
Isliye:
2 ^ 3 ^ 2 ^ 4 ^ 3
= (2 ^ 2) ^ (3 ^ 3) ^ 4
= 0 ^ 0 ^ 4
= 4
