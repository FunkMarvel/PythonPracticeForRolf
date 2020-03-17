# Exercise 2.17, author Anders P. Åsbø.
# solution to a):
# using the same code as in 2.9 to generate the t and y values.
n = 10
i = 0

v0 = 4.0
g = 1.62

ts = 2.0*v0/g
dt = ts/n

T = []
Y = []

while i < n + 1:
    t = i*dt
    T.append(t)
    y = v0*t - (1.0/2.0)*g*(t**2)
    Y.append(y)
    i = i + 1

ty1 = [T, Y]  # creating nested list 1.

print("a)" '\n' "t:  |y:")  # adding headers.
for i in range(len(ty1[0])):  # printing the table from a nested list with columns.
    print("%.2f|%.2f" % (ty1[0][i], ty1[1][i]))

print("---------")  # adding a break between the two running examples.

# solution to b):
ty2 = []  # creating nested list 2.

for t, y in zip(T, Y):  # adding the table rows to ty2.
    ty2.append([t, y])

print("b)" '\n' "t:  |y:")  # adding headers.
for i in range(len(ty2)):  # printing the table from a nested list with rows.
    print("%.2f|%.2f" % (ty2[i][0], ty2[i][1]))

# running examples:
"""
$ python3 ball_table3.py
a)
t:  |y:
0.00|0.00
0.49|1.78
0.99|3.16
1.48|4.15
1.98|4.74
2.47|4.94
2.96|4.74
3.46|4.15
3.95|3.16
4.44|1.78
4.94|0.00
---------
b)
t:  |y:
0.00|0.00
0.49|1.78
0.99|3.16
1.48|4.15
1.98|4.74
2.47|4.94
2.96|4.74
3.46|4.15
3.95|3.16
4.44|1.78
4.94|0.00
"""
