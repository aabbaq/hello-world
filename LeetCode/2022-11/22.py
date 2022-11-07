class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def search(_res, left, right):
            if len(_res) == 2*n:
                res.append(''.join(_res))
                return
            if left < n:
                _res.append('(')
                search(_res, left+1, right)
                _res.pop()
            if right < left:
                _res.append(')')
                search(_res, left, right+1)
                _res.pop()
        
        search([], 0, 0)
        return res