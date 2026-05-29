import math


class Solution:
    def minElement(self, nums: list[int]) -> int:
        ans = math.inf
        for n in nums:
            cur = 0
            flg = True
            while n > 0:
                cur += n % 10
                n //= 10
                if cur >= ans:
                    flg = False
                    break
            if flg:
                ans = cur
        return ans
