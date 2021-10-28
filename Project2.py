from math import exp
import random
# C1: average = 9, standard deviation = 3
# C2: average = 7, standard deviation = 5
# C3: average = 11, standard deviation = 7
C1mean = 9
C1std = 3
C2mean = 7
C2std = 5
C3mean = 11
C3std = 7

def exploitOnly():
    list = [random.normalvariate(C1mean, C1std), random.normalvariate(C2mean, C2std), random.normalvariate(C3mean, C3std)]
    if max(list) == list[0]:
        list.extend([random.normalvariate(C1mean,C1std) for i in range(297)])
    if max(list) == list[1]:
        list.extend([random.normalvariate(C2mean,C2std) for i in range(297)])
    if max(list) == list[2]:
        list.extend([random.normalvariate(C3mean,C3std) for i in range(297)])
    #return list
    return sum(list,0)

print(exploitOnly())
#print(len(exploitOnly()))

def exploreOnly():
    list = [random.normalvariate(C1mean,C1std) for i in range(100)]
    list.extend([random.normalvariate(C2mean,C2std) for i in range(100)])
    list.extend([random.normalvariate(C3mean,C3std) for i in range(100)])
    #return list
    return sum(list,0)

print(exploreOnly())

def eGreedy(p1:int):
    list = [random.normalvariate(C1mean, C1std), random.normalvariate(C2mean, C2std), random.normalvariate(C3mean, C3std)]
    if max(list) == list[0]:
        list.extend([random.normalvariate(C1mean,C1std) for i in range(round((100-p1)/100*297))])
        list.extend(random.choice([random.normalvariate(C1mean,C1std),random.normalvariate(C2mean,C2std),random.normalvariate(C3mean,C3std)]) for i in range(round((p1)/100*297)))
    elif max(list) == list[1]:
        list.extend([random.normalvariate(C2mean,C2std) for i in range(297)])
        list.extend(random.choice([random.normalvariate(C1mean,C1std),random.normalvariate(C2mean,C2std),random.normalvariate(C3mean,C3std)]) for i in range(round((p1)/100*297)))
    elif max(list) == list[2]:
        list.extend([random.normalvariate(C3mean,C3std) for i in range(297)])
        list.extend(random.choice([random.normalvariate(C1mean,C1std),random.normalvariate(C2mean,C2std),random.normalvariate(C3mean,C3std)]) for i in range(round((p1)/100*297)))
    #return list
    return sum(list,0)

print(eGreedy(2))

