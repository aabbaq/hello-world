class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counter = collections.Counter(s)
        res = []
        for c in order:
            if c in counter.keys():
                res.append(c * counter[c])
                counter[c] = 0
        for key, count in counter.items():
            if count != 0:
                res.append(key * count)
        return ''.join(res)