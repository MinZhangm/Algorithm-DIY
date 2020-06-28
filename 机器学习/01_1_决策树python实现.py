import numpy as np
from numpy import random

def entropy(x):
  res =  0
  for i in x:
    res -= i*np.log2(i)
  return res
# np中log()底数为e,log10(), log2(),直接调用.

def 
