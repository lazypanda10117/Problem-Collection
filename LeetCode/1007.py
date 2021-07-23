class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        DOM_NUM = 6
        total_len = len(tops)
        
        counts_top = [0 for _ in range(DOM_NUM)]
        counts_bottom = [0 for _ in range(DOM_NUM)]
        counts = [0 for _ in range(DOM_NUM)]
        for idx in range(total_len):
            top_idx = tops[idx] - 1
            bottom_idx = bottoms[idx] - 1
            counts_top[top_idx] += 1
            counts_bottom[bottom_idx] += 1
            if top_idx == bottom_idx:
                counts[top_idx] += 1
            else:
                counts[top_idx] += 1
                counts[bottom_idx] += 1
        
        min_flip = 100000
        for c in range(DOM_NUM):
            if counts[c] == total_len:
                intersection = counts_top[c] + counts_bottom[c] - total_len
                min_flip = min(min_flip, min(counts_top[c] - intersection, counts_bottom[c] - intersection))
        
        if min_flip == 100000:
            return -1
        return min_flip