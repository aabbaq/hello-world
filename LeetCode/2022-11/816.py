import itertools as it
class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        res = []
        def generate(_s):
            _res = []
            if _s[0] != '0' or _s == '0':
                _res.append(_s)
            for i in range(1, len(_s)):
                if i != 1 and _s[0] == '0' or _s[-1] == '0':
                    continue
                _res.append(_s[:i] + '.' + _s[i:])
            return _res
        
        s = s[1:-1]
        l = len(s)
        for i in range(1, l):
            x = generate(s[:i])
            if x == []:
                continue
            y = generate(s[i:])
            if y == []:
                continue
            for j,k in it.product(x,y):
                res.append('('+j+', '+k+')')
        return res