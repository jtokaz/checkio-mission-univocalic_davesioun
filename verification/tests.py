import random

TESTS = {"Basic": [
    {"input": [0,11], "answer": 11},
    {"input": [14,0], "answer": 14},
    {"input": [22,4], "answer": 22},
]}

R = range(0,100)
for x,y in zip(random.sample(R,10),random.sample(R,10)):
    TESTS["Basic"].append({"input": [x,y], "answer": max(x,y)})
R = range(0,2000000001)
for x,y in zip(random.sample(R,20),random.sample(R,20)):
    TESTS["Basic"].append({"input": [x,y], "answer": max(x,y)})
