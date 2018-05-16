import matplotlib.pyplot as plt
from matplotlib.pyplot import *
import numpy as np

class Atom():
    def __init__(self, th=None, t=None):
        self.th = th
        self.t = t

def readData(file):
    f = open(file, 'r')
    res, lines = [], [ line[:-1] for line in f ]        # store lines in this list without newline
    for line in lines:
        num = line.split(':')[1]
        if 'THREADS' in line:
            atom = Atom()
            atom.th = int(num)
        elif 'TIME' in line:
            atom.t = float(num)
        elif 'SUM' in line:
            res.append(atom)
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

d1 = getdata('s_c_1_10000.out')
d2 = getdata('s_c_256_10000.out')
d3 = getdata('s_c_512_10000.out')
d4 = getdata('s_c_1024_10000.out')
d5 = getdata('s_c_1_100000.out')
d6 = getdata('s_c_256_100000.out')
d7 = getdata('s_c_512_100000.out')
d8 = getdata('s_c_1024_100000.out')
d9 = getdata('s_c_1_1000000.out')
d10 = getdata('s_c_256_1000000.out')
d11 = getdata('s_c_512_1000000.out')
d12 = getdata('s_c_1024_1000000.out')

p1, = plt.plot(d1[0], d1[1], 'g:')
p2, = plt.plot(d2[0], d2[1], 'g-.')
p3, = plt.plot(d3[0], d3[1], 'g--')
p4, = plt.plot(d4[0], d4[1], 'g')
p5, = plt.plot(d5[0], d5[1], 'b:')
p6, = plt.plot(d6[0], d6[1], 'b-.')
p7, = plt.plot(d7[0], d7[1], 'b--')
p8, = plt.plot(d8[0], d8[1], 'b')
p9, = plt.plot(d9[0], d9[1], 'r:')
p10, = plt.plot(d10[0], d10[1], 'r-.')
p11, = plt.plot(d11[0], d11[1], 'r--')
p12, = plt.plot(d12[0], d12[1], 'r')

P = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12]
L = ["scount_1_10000", "scount_256_10000", "scount_512_10000", "scount_1024_10000",
     "scount_1_100000", "scount_256_100000", "scount_512_100000", "scount_1024_100000",
     "scount_1_1000000", "scount_256_1000000", "scount_512_1000000", "scount_1024_1000000"]
legend(P, L)


plt.xlabel('Number of Threads')
plt.ylabel('Average Execution Time of 10 runs (second)')

plt.xticks(np.arange(0, 101, 5.0), fontsize=8)
plt.yticks(np.arange(0, 5.2, 0.2), fontsize=8)

plt.title('Performance of the Correct Sloppy Counter')
plt.show()


