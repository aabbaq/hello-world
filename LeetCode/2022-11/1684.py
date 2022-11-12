class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res = 0
        for word in words:
            for c in word:
                if c not in allowed: 
                    break
            else:
                res += 1
        return res