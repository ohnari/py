import numpy as np

quote = [[0] for i in range(3)]
xp = np.array(quote)
xq = np.array(xp)
print(xp, xq)
xq = np.append(xq, [[9], [9], [9]], axis=1)
print(xq)
