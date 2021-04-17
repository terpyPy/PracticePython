import numpy as np
import random

'''
    -2D array, 2 columns-
  column 1   column 2    
[[0.54879803 0.21665792] row 1   axis = 1
 [0.14832017 0.8947242 ] row 2    
 [0.76910123 0.6972656 ]] row 3
  axis = 0
 (3 rows,2 columns) x = rows, y = columns z = dimensions
'''

x = random.randrange(1,100)
def primes(n):
    """Copied from https://stackoverflow.com/a/16996439/5393381 (author: Daniel Fischer)"""
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)
            n //= d
        d += 1
    if n > 1:
        primfac.append(n)
    return primfac

if x > 1:

    # Iterate from 2 to n / 2
    for i in range(2, x):

        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
        if (x % i) == 0:
            #print(x, i, "is not a prime number 1")
            y = x//i
            z = i
            break
    else:
        #print(x, "is a prime number 2")
        y = 1
        z = i

else:
    z = 1
    y = 1
    print(x, "is not a prime number 3")
newList = [x//z if x != 1 else primes(x)]
newList2 = [primes(z) if x == 1 else z]
numArray = np.arange(0, x, dtype='i4').reshape(int(newList[0]), -1, int(newList2[0]))


strArray = np.array([0]*x).reshape(int(newList[0]), -1, z)
#print(y, x, x//y)
#print(np.var(numArray, axis=0))

conjugateTwoArrays = np.concatenate([numArray, strArray])  # make both arrays
# 2d along, then concatenate them together along the column axis
newArray = np.array(conjugateTwoArrays)
print(np.concatenate([conjugateTwoArrays, newArray]))
print(conjugateTwoArrays)
print(conjugateTwoArrays.shape)

print(newArray)
print(newArray.shape)
