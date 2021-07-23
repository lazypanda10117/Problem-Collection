class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1_lst = version1.split('.')
        v2_lst = version2.split('.')
        return self.customCompare(v1_lst, v2_lst)

    def customCompare(self, lst1, lst2):
        # normalize list
        l1, l2 = lst1, lst2
        if len(lst1) < len(lst2):
            l1.extend([0 for _ in range(len(lst2) - len(lst1))])
        else:
            l2.extend([0 for _ in range(len(lst1) - len(lst2))])
            
        for idx, n1 in enumerate(l1):
            n2 = l2[idx]     
            if int(n1) < int(n2):
                return -1
            elif int(n1) > int(n2):
                return 1
            else:
                pass
        return 0
