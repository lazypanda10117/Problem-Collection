class Solution:
    def operation(self, num):
        if len(num) == 0:
            return []
        result = [num]
        for i in range(1,len(num)+1):
            numi = num[:i]
            for rest in self.operation(num[i:]):
                result.append(f"{numi}+{rest}")
                result.append(f"{numi}-{rest}")
                result.append(f"{numi}*{rest}")
        return result

    def addOperators(self, num: str, target: int) -> List[str]:
        ops = self.operation(num)
        result = []
        for r in ops:
            expr = re.compile("(^|\+|\-|\*)0{2,}(\+|\-|\*|$)")
            temp = expr.search(r)
            if temp:
                continue
            try:
                if eval(r) == target:
                    result.append(r)
            except SyntaxError as e:
                continue
        return result