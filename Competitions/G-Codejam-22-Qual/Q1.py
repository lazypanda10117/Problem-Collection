import sys

num_cases = int(sys.stdin.readline())

def build_row_1(C, is_first=False):
    result = ""
    for i in range(C*2+1):
        if i % 2 == 0:
            result += "+"
        else:
            result += "-"
    if is_first:
        result = ".." + result[2:]
    return result
        
def build_row_2(C, is_first=False):
    result = ""
    for i in range(C*2+1):
        if i % 2 == 0:
            result += "|"
        else:
            result += "."
    if is_first:
        result = "." + result[1:]
    return result

for n in range(num_cases):
    R,C = sys.stdin.readline().split()
    R,C = int(R), int(C)
    print(f"Case #{n+1}:")
    for i in range(2*R+1):
        if i % 2 == 0:
            print(build_row_1(C, i==0))
        else:
            print(build_row_2(C, i==1))
