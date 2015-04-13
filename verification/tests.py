"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

#This is very basic solution.
def factorial(num):
    if num==0: return 1
    return num*factorial(num-1)

TESTS = {"Basic":[
	{"input": 0, "answer": 1},
	{"input": 1, "answer": 1},
	{"input": 2, "answer": 2},
]}
import random

for n in random.sample(range(3, 200), 30):
    TESTS["Basic"].append({"input": n, "answer": factorial(n)})
