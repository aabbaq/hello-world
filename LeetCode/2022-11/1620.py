class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        max_x = max([tower[0] for tower in towers])
        max_y = max([tower[1] for tower in towers])
        res = []
        strength = -1

        for i in range(max_x+1):
            for j in range(max_y+1):
                _strength = 0
                for x,y,q in towers:
                    distance = math.sqrt(abs(i-x)**2 + abs(j-y)**2)
                    if distance <= radius:
                        _strength += math.floor(q / (1+distance))
                if _strength > strength:
                    res = [i, j]
                    strength = _strength
        
        return res