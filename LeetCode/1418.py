class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        MENU = []
        ot = {}
        for order in orders:
            table = order[1]
            item = order[2]
            if table not in ot:
                ot[table] = {}
            if item not in ot[table]:
                ot[table][item] = 0
            ot[table][item] = ot[table][item]+1
            if item not in MENU:
                MENU.append(item)
        MENU.sort()
        result = [["Table"] + MENU]
        for table, item in sorted(ot.items(), key=lambda x: int(x[0])):
            temp = [table]
            for m in MENU:
                if m in item:
                    temp.append(str(item[m]))
                else:
                    temp.append(str(0))
            result.append(temp)
        return result
