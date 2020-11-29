class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        result = []
        P = [i for i in range(1,m+1)]
        for q in queries:
            idx = P.index(q)
            result.append(idx)
            P = [P[idx]] + P[:idx] + P[idx+1:]
        return result
