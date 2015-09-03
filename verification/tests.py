import random

TESTS = {"Basic": [
    {"input": 0, "answer": 0},
    {"input": 9, "answer": 0.9},
    {"input": 41, "answer": 4.1},
    {"input": 65, "answer": 6.5},
    {"input": 79, "answer": 7.9},
]}


for x in random.sample(range(0,1000),10):
    TESTS["Basic"].append({"input": x, "answer": x/10})
R = range(0,2000000001)
for x in random.sample(range(0,2000000000),30):
    TESTS["Basic"].append({"input": x, "answer": x/10})
