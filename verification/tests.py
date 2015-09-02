import random

TESTS = {"Basic": [
    {"input": 0, "answer": 0},
    {"input": 9, "answer": 0},
    {"input": 41, "answer": 4},
    {"input": 65, "answer": 6},
    {"input": 79, "answer": 7},
]}


for x in random.sample(range(0,1000),10):
    TESTS["Basic"].append({"input": x, "answer": x//10})
R = range(0,2000000001)
for x in random.sample(range(0,2000000000),30):
    TESTS["Basic"].append({"input": x, "answer": x//10})
