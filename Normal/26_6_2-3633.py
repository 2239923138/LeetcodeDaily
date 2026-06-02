from math import inf

class Solution:
    def earliestFinishTime(
        self,
        landStartTime: list[int],
        landDuration: list[int],
        waterStartTime: list[int],
        waterDuration: list[int],
    ) -> int:
        n, m = len(landDuration), len(waterDuration)
        landEnd = min(landStartTime[i] + landDuration[i] for i in range(n))
        waterEnd = min(waterStartTime[i] + waterDuration[i] for i in range(m))

        landans = waterans = inf

        for i in range(m):
            landans = min(landans, max(landEnd, waterStartTime[i]) + waterDuration[i])

        for i in range(n):
            waterans = min(waterans, max(waterEnd, landStartTime[i]) + landDuration[i])
        return min(landans, waterans)
