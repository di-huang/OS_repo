import matplotlib.pyplot as plt
from matplotlib.pyplot import *
import numpy as np

class Atom():
    def __init__(self, th=None, c=None, t=None, s=None):
        self.th = th
        self.c = c
        self.t = t
        self.s = s

def readData(file):
    f = open(file, 'r')
    res, lines = [], [ line[:-1] for line in f ]        # store lines in this list without newline
    for line in lines:
        num = line.split(':')[1]
        if 'THREADS' in line:
            atom = Atom()
            atom.th = int(num)
        elif 'COUNT PER THREAD' in line:
            atom.c = int(num)
        elif 'TIME' in line:
            atom.t = float(num)
        elif 'SUM' in line:
            atom.s = int(num)
            res.append(atom)
        else:
            print('some error0 occurs')
    return res

def getdata(file):
    data = readData(file)
    x, y = [None for i in range(100)], [None for j in range(100)]
    for i in range(0, 100*10, 10):
        s, th = 0, data[i].th
        for j in range(10):
            s += data[i+j].t
        x[i//10] = th
        y[i//10] = s / 10
    return x, y

d1 = getdata('p_c_10000.out')
d2 = getdata('p_c_100000.out')
d3 = getdata('p_c_1000000.out')

p1, = plt.plot(d1[0], d1[1], color='g')
p2, = plt.plot(d2[0], d2[1], color='b')
p3, = plt.plot(d3[0], d3[1], color='r')
legend([p1, p2, p3], ["pcount_10000", "pcount_100000", "pcount_1000000"])

plt.xlabel('Number of Threads')
plt.ylabel('Average Execution Time of 10 runs (second)')

plt.xticks(np.arange(0, 101, 5.0), fontsize=8)
plt.yticks(np.arange(0, 2.6, 0.2), fontsize=8)

plt.title('Performance of the Precise Counter')
plt.show()

# print(d1[1][0])











