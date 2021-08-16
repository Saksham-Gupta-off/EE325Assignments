import numpy as np
import matplotlib.pyplot as plt

def find_prob(fname):
    with open(fname) as f:
        data = f.readlines()
    prob = np.array([])
    val = np.array([])
    for i in range(0, len(data)):
        val = 0 if data[i]=='false\n' else 1
        if(i==0):
            prob = np.append(prob, val)
        else:
            prob = np.append(prob, (prob[i-1]*i + val)/(i+1))
    for i in range(n, len(prob)):
        if (prob[i] < pH-sr):
            print("SURE: " + str(i+1) + " with probability " + str(prob[i]))
        elif (prob[i] < pH-dt):
            print("Doubt: " + str(i+1) + " with probability " + str(prob[i]))


# initial assumption
pH = 0.5

# initial gap of n elements
n = 10

# buffer for doubt
dt = 0.1

# buffer for sure
sr = 0.25

print(find_prob("hw1b1.txt"))
print("\n\n")
print(find_prob("hw1b2.txt"))
print("\n\n")
print(find_prob("hw1b3.txt"))
print("\n\n")
print(find_prob("hw1b4.txt"))