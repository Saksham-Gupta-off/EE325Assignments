import numpy as np
import matplotlib.pyplot as plt

k = 200
# change value of k here

data = np.loadtxt("hw1a.txt")
avg1 = np.array([])
std1 = np.array([])
avg2 = np.array([])
std2 = np.array([])
avg3 = np.array([])
std3 = np.array([])

for i in range(0,50):

    opt1 = data[0:k]
    avg1 = np.append(avg1, np.mean(opt1))
    std1 = np.append(std1, np.std(opt1))

    rand = int(np.random.random() * (10000-k))
    opt2 = data[rand:(rand+k)]
    avg2 = np.append(avg2, np.mean(opt2))
    std2 = np.append(std2, np.std(opt2))

    opt3 = np.random.choice(data,k,replace=False)
    avg3 = np.append(avg3, np.mean(opt3))
    std3 = np.append(std3, np.std(opt3))

print("Assuming Case 3 is best:-\n" + "average: " + str(np.mean(avg3)) + "\nstddev: " + str(np.mean(std3)))

fig, ax = plt.subplots(1,3)
index = range(1,51)
ax[0].scatter(index, avg1)
ax[1].scatter(index, avg2)
ax[2].scatter(index, avg3)
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, wspace=0.4, hspace=0.4)
plt.show()
