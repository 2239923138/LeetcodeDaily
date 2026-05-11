"""
2553. 分割数组中数字的数位

给你一个正整数数组 nums ，请你返回一个数组 answer ，你需要将 nums 中每个整数进行数位分割后，按照 nums 中出现的 相同顺序 放入答案数组中。

对一个整数进行数位分割，指的是将整数各个数位按原本出现的顺序排列成数组。

比方说，整数 10921 ，分割它的各个数位得到 [1,0,9,2,1] 。

1 <= nums.length <= 1000
1 <= nums[i] <= 105
"""


def seperateNum(n):
    ret = []
    while n > 0:
        ret.append(n % 10)
        n //= 10
    return ret[::-1]


class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            ans += seperateNum(num)
        return ans
