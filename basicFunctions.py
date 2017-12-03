import os

def mySum(data):
    totalSum = 0
    for i in range(len(data)):
        totalSum += data[i]
    return totalSum

data = [1,2,3,4,5,6,7,8]
print(data)
os.system("CLS")
total = mySum(data)
print(total)