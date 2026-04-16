"""
1423. 可获得的最大点数

几张卡牌 排成一行，每张卡牌都有一个对应的点数。点数由整数数组 cardPoints 给出。

每次行动，你可以从行的开头或者末尾拿一张卡牌，最终你必须正好拿 k 张卡牌。

你的点数就是你拿到手中的所有卡牌的点数之和。

给你一个整数数组 cardPoints 和整数 k，请你返回可以获得的最大点数。

1 <= cardPoints.length <= 10^5
1 <= cardPoints[i] <= 10^4
1 <= k <= cardPoints.length
"""


class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        n = len(cardPoints)
        if k == n:
            return sum(cardPoints)
        k = n - k
        s = 0
        ans = float("inf")
        for i, x in enumerate(cardPoints):
            s += x
            if i - k + 1 < 0:
                continue

            ans = min(ans, s)
            s -= cardPoints[i - k + 1]
        return int(sum(cardPoints) - ans)
