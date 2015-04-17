import random

def factorial(num):
    # This is very basic solution.
    return num * factorial(num - 1) if num else 0


TESTS = {"Basic": [
    {"input": 0, "answer": 1},
    {"input": 1, "answer": 1},
    {"input": 2, "answer": 2},
]}


for n in random.sample(range(3, 100), 30):
    TESTS["Basic"].append({"input": n, "answer": factorial(n)})
