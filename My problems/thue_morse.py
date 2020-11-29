from multiprocessing import Pool, shared_memory
from functools import reduce

def debugAtInterval(n, interval, message, *args):
    if not (n % interval):
        print(message.format(*args))

class Generator1:
    def __init__(self):
        self.base_case = "0"

    def generateKString(self, n, result):
        def nextIter(s):
            sComp = ""
            for c in s:
                sComp += "1" if c == "0" else "0"
            s += sComp
            return s
        return result if n == 0 else self.generateKString(n-1, nextIter(result))

    def tripleRepeatChecker(self, kString):
        # Loop through all the possible substring lengths
        for i in range(1, int(len(kString)/3) + 1):
            debugAtInterval(i, 100, "Substring Length {}", i)
            # Loop through all the possible starting position
            for j in range(len(kString)-(3*i)+1):
                if kString[j: j+i] == kString[j+i: j+2*i] and \
                kString[j+i: j+2*i] == kString[j+2*i: j+3*i]:
                    print("Repeat At: {}".format(j))
                    return True
        return False

    def check(self, n):
        return self.tripleRepeatChecker(self.generateKString(n, self.base_case))


class Generator2:
    def __init__(self, n, processor):
        self.base_case = "0"
        self.kString = self.generateKString(n, self.base_case)
        self.processor = processor

    def generateKString(self, n, result):
        def nextIter(s):
            sComp = ""
            for c in s:
                sComp += "1" if c == "0" else "0"
            s += sComp
            return s
        return result if n == 0 else self.generateKString(n-1, nextIter(result))
    
    def check(self, offset):
        for i in range(1, int(len(self.kString)/3) + 1):
            # Loop through all the possible starting position
            debugAtInterval(i, 100, "Substring Length {}", i)
            j = offset
            while j < len(self.kString)-(3*i)+1:
                if self.kString[j: j+i] == self.kString[j+i: j+2*i] and \
                self.kString[j+i: j+2*i] == self.kString[j+2*i: j+3*i]:
                    return True
                j = j + self.processor
        return False

Iteration = 16

def main():
    print("Iteration {} Result: {}".format(Iteration, Generator1().check(Iteration)))

def mainMP():
    processNum = 6
    pool = Pool(processes=processNum)
    mpGenerator = Generator2(Iteration, processNum)
    results = pool.map(mpGenerator.check, range(processNum))
    print("Iteration {} Result: {}".format(Iteration, reduce(lambda x,y: x or y, results)))

# main()
mainMP()