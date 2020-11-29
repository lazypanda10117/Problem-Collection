class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        l = list([("a",a),("b",b),("c",c)])
        l = sorted(l, key=lambda x: x[1])
        small_sum = l[0][1]+l[1][1]
        maxN = l[2][1]
        if 2*(small_sum)+2 < l[2][1]:
            maxN = 2*(small_sum)+2
        result = ""
        l1 = maxN
        l2 = small_sum

        while not (l1 == 0 or l2 == 0):
            result += l[2][0]
            l1 -= 1
            if l1 > l2:
                result += l[2][0]
                l1 -= 1
            else:
                if l2 > l[0][1]:
                    result += l[1][0]
                else:
                    result += l[0][0]
                l2 -= 1
            if l2 > 0:
                if l2 > l[0][1]:
                    result += l[1][0]
                else:
                    result += l[0][0]
                l2 -= 1
        result += l[2][0]*l1
        return result
