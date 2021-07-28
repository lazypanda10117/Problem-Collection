import math

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        counts = defaultdict(int)
        for i in deck:
            counts[i] += 1
        if len(counts) == 1:
            return counts[deck[0]] > 1
        return math.gcd(*list(counts.values())) > 1
