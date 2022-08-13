
"""

@author: UNISEPP
"""

# Testing the law of the large numbers using normal distribution
# N random normally distributed numbers with stedv = 1 and mean = 0
# How many of these numbers fall between -1 and 1 and divide by total N
# We know that E(x) = 68.2 %
# Mean(x) -> E(x) as we incrrease N

import numpy as np


n = [10 , 100 , 1000 , 10000 , 100000 , 1000000 , 10000000]
for i in n:
  temp =0
  for j in np.random.randn(i) :
    if j<1 and j >-1 :
        temp +=1
  print(temp/i)     






















