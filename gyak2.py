import numpy
import numpy as np
import matplotlib.pyplot as plt

def osszead(a, b):
    return a + b

osszead(3,4)

r_eff = np.array([[0.1, 0.2], [0.3, 0.4], [0.5, 0.6]])
IC = np.exp(r_eff)
#print(type(a))
print(IC)

IC_2y = IC**2
r_2y = np.log(IC_2y)
print(r_2y)

print(r_eff.shape)


a_elso = np.array([[1, 2], [2, 5], [2, 8]])
print(np.sum(a_elso))
print(np.sum(a_elso, axis=0))
print(np.sum(a_elso, axis=1))

print(np.mean(a_elso, axis=0))
print(np.std(a_elso, axis=0))
print(np.min(a_elso, axis=0))
print(np.max(a_elso, axis=0))
print(np.diff(a_elso, axis=0))

c = a_elso - np.mean(a_elso)
print(c)
print(np.mean(c))
print(c.mean())

is_pos = c>0
print(is_pos)

d = c.copy()

d[is_pos] += 100
print(d)
print(c)

a_new = np.array([[2, 2], [2, 4], [0, 4]])
print(a_new.std(axis=1))
print(a_new.std(axis=1, ddof=0))
print(a_new.std(axis=1, ddof=1))

#random numbers
np.random.seed(112)
a_rnd_uniform = np.random.random((3, 2))
print(a_rnd_uniform)
a_rnd_normal = np.random.normal([1, 8.2], [1, 1], (10, 2))
print(a_rnd_normal)

reszvenyek = np.random.normal([0.05, 0.1], [0.1, 0.2], [1000, 2])
#print(reszvenyek)
print(np.mean(reszvenyek, axis=0))
print(np.std(reszvenyek, axis=0))
p0 = np.array([10, 100])
arfolyamok =  p0 * np.exp(reszvenyek)
#print(arfolyamok)

plt.hist(arfolyamok[:, 1], bins=100)
plt.figure()
plt.scatter(arfolyamok[:, 0], arfolyamok[:, 1])
plt.show()