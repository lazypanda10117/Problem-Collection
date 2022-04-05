import sys


class Node:
    def __init__(self, fun, parent):
        self.child = []
        self.parent = parent
        self.fun = fun


def get_max_fun():
    N = int(sys.stdin.readline())
    F = [int(x) for x in sys.stdin.readline().split()]
    P = [int(x) for x in sys.stdin.readline().split()]
    n_map = {i+1: Node(F[i], P[i] if P[i] > 0 else None) for i in range(N)}
    roots = []

    for idx, parent_id in enumerate(P):
        id = idx+1
        node = n_map[id]
        if node.parent in n_map:
            parent = n_map[node.parent]
            parent.child.append(node)
        else:
            roots.append(node)

    def recurse(root):
        # tuple = (subtree path sum, first path maximum)
        if len(root.child) == 0:
            return (root.fun, root.fun)

        sp = []
        fp = []
        for c in root.child:
            tup = recurse(c)
            sp.append(tup[0])
            fp.append(tup[1])
        
        subtree_sum = sum(sp)
        min_first_path = min(fp)
        added_val = max(root.fun - min_first_path, 0)
        new_min_first_path = max(min_first_path, root.fun)
        return (subtree_sum + added_val, new_min_first_path) 

    total_fun = 0
    for root in roots:
        sub_sum, min_first_path = recurse(root)
        total_fun += sub_sum

    print(f"Case #{n+1}: {total_fun}")
    

num_cases = int(sys.stdin.readline())
for n in range(num_cases):
    get_max_fun()

