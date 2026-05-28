import math


class Trie:
    __slots__ = "son", "min_len", "best_idx"

    def __init__(self):
        self.son = [None] * 26
        self.min_len = math.inf


class Solution:
    def stringIndices(
        self, wordsContainer: list[str], wordsQuery: list[str]
    ) -> list[int]:
        ordA = ord("a")
        root = Trie()
        for i, q in enumerate(wordsContainer):
            len_q = len(q)
            if len_q < root.min_len:
                root.min_len = len_q
                root.best_idx = i

            cur = root
            for ch in reversed(q):
                c = ord(ch) - ordA
                if cur.son[c] is None:
                    cur.son[c] = Trie()
                cur = cur.son[c]

                if len_q < cur.min_len:
                    cur.min_len = len_q
                    cur.best_idx = i

        ans = []
        for s in wordsQuery:
            cur = root
            for ch in reversed(s):
                c = ord(ch) - ordA
                if cur.son[c] is None:
                    break
                cur = cur.son[c]
            ans.append(cur.best_idx)
        return ans
