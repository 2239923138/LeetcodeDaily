class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        preA, preB = set(), set()
        n = len(A)
        ans = [0] * (n + 1)
        for i in range(n):
            a, b = A[i], B[i]
            if a == b:
                ans[i + 1] = ans[i] + 1
            else:
                ans[i + 1] = ans[i] + (a in preB) + (b in preA)
            preA.add(a)
            preB.add(b)
        return ans[1:]
