class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        stack = {'c':0, 'r':0, 'o':0, 'a':0, 'k':0}
        max_count = 0
        count = 0
        i = 0
        c = croakOfFrogs
        while i < len(c):
            if c[i] == 'c':
                stack['c'] += 1
                count += 1
                if count > max_count:
                    max_count = count
            elif c[i] == 'r':
                if stack['c'] > 0:
                    stack['c'] -= 1
                    stack['r'] += 1
                else:
                    return -1
            elif c[i] == 'o':
                if stack['r'] > 0:
                    stack['r'] -= 1
                    stack['o'] += 1
                else:
                    return -1
            elif c[i] == 'a':
                if stack['o'] > 0:
                    stack['o'] -= 1
                    stack['a'] += 1
                else:
                    return -1
            elif c[i] == 'k':
                if stack['a'] > 0:
                    stack['a'] -= 1
                    stack['k'] += 1
                else:
                    return -1
                count -= 1
            i += 1
        del stack['k']
        if sum(stack.values()) > 0:
            return -1

        return max_count
