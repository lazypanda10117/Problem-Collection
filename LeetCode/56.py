class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: (x[0], x[1]))
        merged = []
        cur_min = intervals[0][0]
        cur_max = intervals[0][1]
        for interval in intervals:
            if interval[0] <= cur_max:
                if interval[1] > cur_max:
                    # extend interval, update cur_max
                    cur_max = interval[1]
                else:
                    # do nothing
                    pass
            else:
                # push old_interval
                merged.append([cur_min, cur_max])
                # new interval
                cur_min = interval[0]
                cur_max = interval[1]
        merged.append([cur_min, cur_max])
        return merged
