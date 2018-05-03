import random

d = {1:1, 2:5, 7:2, 4:6, 9:6}
print(max(d.items(), key=lambda x: x[1])[0])
print(max(d.items(), key=lambda x: x[1]))
x = []

for k, v in d.items():
    if v == 6:
        x.append(k)
action = x[random.randint(0, len(x) - 1)]
print x
print action