from time import time
lowVal= 3 # can be userinput
highVal= 5 # can be userinput
start = time()
for i in range(1,101):
    if i % (lowVal * highVal) == 0:
        print('FizzBuzz')
    elif (i % lowVal== 0):
        print('Fizz')
    elif i % highVal== 0 :
        print('Buzz')
    else:
        print(i)
print('runtime:', time() - start)