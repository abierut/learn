import numpy as np
x = np.array([0,1,2])
y = np.array([0,1])

probs = np.array([])
pairs = []
for numx in x:
    for numy in y:
        pairs.append((numx,numy))
        probs = np.append(probs,(numx + numy))
print(pairs)
print(probs)
print(probs.sum())
print ((probs/probs.sum()).sum())

total = 0
for ind, val in enumerate(probs):
    if pairs[ind][1]== 1:
        total += val/probs.sum()
print(total)
"""
for ind, val in enumerate(probs):
    #if pairs[ind][1]== pairs[ind][0]:
    variance.append(((pairs[ind][0] - total)**2)*val/probs.sum())

print(sum(variance))
"""
test2 = np.array([[4,0,2,8],[3,2,0,2],[2,0,1,4]])
print(test2[:,3].sum())
probs2 = test2/test2.sum()
x = np.array([probs2[:,ind].sum() for ind in range(len(probs2[0]))])
y = np.array([probs2[ind].sum() for ind in range(len(probs2))])
print (probs2)
print (x)
print (y)