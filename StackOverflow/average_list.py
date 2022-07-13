import numpy as np
from scipy import stats

tempList = np.array([[95, 132], [96, 132], [94, 133], [134, 239], [95, 131]])

z= stats.zscore(tempList, axis=0)
z = list([abs(x)<1 and abs(y)<1 for x,y in z])

newList = tempList[[not x for x in z]]
tempList = tempList[z]

newList = np.concatenate([[tempList.mean(axis=0)], newList])
print(newList)

# myPoints = np.array([[95, 132], [95, 132], [95, 239], [94, 132]])
# pointMean = myPoints.mean(axis=0)
# print(pointMean)

# print(np.all(abs(z)<1, axis=1))
# print(tempList[np.all(abs(z) < 1, axis=1)])

x = [True, True, False, True]
print(x, [not y for y in x])