from collections import deque

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        cities = {i: False for i in range(len(isConnected))}
        num_city = 0
        for c in cities.keys():
            if cities[c] == True:
                continue
            num_city += 1
            queue = deque([c])
            while len(queue) > 0:
                cur_city = queue.popleft()
                if cities[cur_city] == True:
                    continue
                cities[cur_city] = True
                for other_city_idx, connected in enumerate(isConnected[cur_city]):
                    if connected:
                        if cities[other_city_idx]:
                            continue
                        queue.append(other_city_idx)
        return num_city