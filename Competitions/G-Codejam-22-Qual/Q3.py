import sys

from collections import deque

num_cases = int(sys.stdin.readline())

for n in range(num_cases):
    num_dice = int(sys.stdin.readline())
    sorted_dices = deque(sorted([int(x) for x in sys.stdin.readline().split()]))
    cur_idx = 0
    while len(sorted_dices) > 0:
        cur_num = sorted_dices.popleft()
        if cur_num > cur_idx:
            cur_idx += 1
    print(f"Case #{n+1}: {cur_idx}")
