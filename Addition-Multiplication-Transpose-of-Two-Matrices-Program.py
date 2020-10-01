# Program 1 :-
# Python Program to Add Two Matrices.

print('Addition of Two Matrices is :')
X = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

Y = [[10, 11, 12],
     [13, 14, 15],
     [16, 17, 18]]

Result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

for i in range(len(X)):
    for j in range(len(X[0])):
        Result[i][j] = X[i][j] + Y[i][j]
for r in Result:
    print(r)
# =-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Program 2 :-
# Python Program to Multiply Two Matrices.

print('Multiplication of Two Matrices is :')
X = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

Y = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

Result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

# iterate through rows of X
for i in range(len(X)):
    for j in range(len(Y[0])):
        for k in range(len(Y)):
            Result[i][j] += X[i][k] * Y[k][j]
for r in Result:
    print(r)
# =-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Program 3 :-
# Python Program to Transpose a Matrix

print('Transpose a Matrix :')
X = [[1, 2],
     [4, 5],
     [3, 4]]

Result = [[0, 0, 0],
          [0, 0, 0]]

# iterate through rows
for i in range(len(X)):
    for j in range(len(X[0])):
        Result[j][i] = X[i][j]

for r in Result:
    print(r)
# =-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
