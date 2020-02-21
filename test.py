from random import choice

import matplotlib
import numpy as np
import pandas as pd

#alt enter after highlighting
#ctrl+Q for quick documentation
#github push is ctrl shift k




# test = 1
#
# # def adder(A, B):
# #     test = A*2+B
# #     print(test)
# #     return
#
# print(test)



x = np.array([2,3,1,5])
y = pd.DataFrame([1,2,3,4,5])

x.shape
y.shape

z = np.array([[1,2,3],[4,5,6]])
z1 = pd.DataFrame([[1,2,3],[4,5,6]])
#z2 = z1.astype(float)
#z3 = z2.astype(int)



# df = pd.DataFrame(np.random.rand(3, 4), columns=list('ABCD'))
# df *= 10
# print(df)

range1 = list(range(3))
#goes from 0-2 since that is 3 long.

#choose columns and rows
z1.iloc[[0,1],[1]]

z1.iloc[1] #column 1, all rows
z1.iloc[[1]] #row 1, all columns

z1.iloc[[1],[1]].shape #gives row, col as (1, 1)

