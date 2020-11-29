from collections import defaultdict

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        character1 = defaultdict(int)
        for c in word1:
            character1[c] += 1
        c1_kset = set(character1.keys())
        c1_vset = set(character1.values())
        character2 = defaultdict(int)
        for c in word2:
            character2[c] += 1
        c2_kset = set(character2.keys())
        c2_vset = set(character2.values())
        
        return c1_kset == c2_kset and c1_vset == c2_vset
