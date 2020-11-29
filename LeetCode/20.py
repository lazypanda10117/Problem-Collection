class Solution:
    def isValid(self, s: str) -> bool:

#         dimension_3_stack = {
#             "1": [],
#             "2": [],
#             "3": [],
#         }
        
#         s_push = (lambda bucket: dimension_3_stack[bucket].append(1))
#         s_pop = (lambda bucket: dimension_3_stack[bucket].pop())
        
        dispatcher = {
            "(": (True, 1),
            ")": (False, 1),
            "{": (True, 2),
            "}": (False, 2),
            "[": (True, 3),
            "]": (False, 3),
        }

        big_stack = list()
        try:
            for p in s:
                if dispatcher.get(p)[0]:
                    big_stack.append(p)
                else:
                    if dispatcher.get(big_stack[-1])[1] == dispatcher.get(p)[1]:
                        big_stack.pop()
                    else:
                        return False
            return not big_stack
        except:
            return False
