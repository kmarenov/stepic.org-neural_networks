import sys
sys.stdin = open('02.txt', 'r')

from urllib.request import urlopen
import numpy as np

f = urlopen(input())

sbux = np.loadtxt(f, skiprows=1, delimiter=",")
print(sbux.mean(axis=0))