"""
Program that uses Cramer's rule to solve a system of three linear equations with three variables.
Written by Anders P. Asbo.
"""
import numpy as np  # importing Numerical Python library, so I can use it's arrays to store matrices and vectors.


def printGenericMatrix(m, n):
    """Prints generic MxN-matrix."""
    for i in range(m):
        print("|", end='')
        for j in range(n):
            print(chr(ord('a') + i*(m+1) + j), end='')
            if j < n-1:
                print(" ", end='')
        print("|")


def getInput(matrix):
    """
    Populates a given MxN-matrix with elements given by the user
    using the command-line.
    """
    m, n = matrix.shape  # get matrix dimensions.

    # iterate over, and set, each matrix element:
    for i in range(m):
        for j in range(n):
            # gets number from terminal:
            koeff = eval(input(f"Skriv inn element '{chr(ord('a') + i*(m+1) + j)}' og trykk 'enter': "))
            matrix[i,j] = koeff  # save number to matrix.
    
    return matrix  # return populated matrix


def printGivenMatrix(matrix):
    """
    Prints the given expanded coefficient matrix as the vector-matrix equation Ax=b,
    where A is the matrix consisting of the first n-1 columns in the input matrix, and
    b is the solution vector consisting of the final column in the input matrix.
    """
    m, n = matrix.shape # get matrix dimensions.

    # prints the system of equations as Ax=b:
    for i in range(m):
        print("|", end='')
        for j in range(n):
            print(f"{matrix[i, j]:4}", end='')
            
            if j < n-1:
                print(" ", end='')
            if (j == n-2) and (i != m-2):
               print(f"| |{chr(ord('x') + i)}|   |", end='')
            elif j == n-2:
                print(f"| |{chr(ord('x') + i)}| = |", end='')

        print("|")


def solve3x3System(matrix):
    """
    Function solving the system of equations, represented by
    the input matrix, by using Cramer's rule.
    """
    m, n = matrix.shape # get matrix dimensions.
    
    determinants = {}  # dictionary for storing determinants.
    for k in range(n):
        A = np.copy(matrix[:,:-1])  # creates A matrix
        if k != 0:  # swaps column number k in A with b-vector:
            A[:,k-1] = np.copy(matrix[:,-1])

        # calculates 3x3 determinant of A_k matrix, where "A0" corresponds to the determinant of A:
        determinants[f"A{k}"] = A[0,0]*A[1,1]*A[2,2] + A[0,1]*A[1,2]*A[2,0] + A[0,2]*A[1,0]*A[2,1] - A[2,0]*A[1,1]*A[0,2] - A[2,1]*A[1,2]*A[0,0] - A[2,2]*A[1,0]*A[0,1]

    xvec = np.zeros(3)  # creates vector to store solution.
    for i in range(len(xvec)):  # iterates through and calculates each unknown as det(A_k)/det(A):
        xvec[i] = determinants[f"A{i}"]/determinants["A0"]

    return xvec  # returns vector containing solutions.


def main():
    """
    Main function of program.
    This is where the program starts executing.
    """
    m, n = 3, 4  # set dimension of expanded coefficient matrix (m rows, n columns).
    expandedCoeffMatrix = np.zeros((m,n))  # creating MxN-matrix filled with zeros.
    
    print("Dette programmet tar inn et likningsystem med 3 likninger\n"
          +"og 3 ukjente i form av en utvidet koeffisientmatrise:")
    
    printGenericMatrix(m,n)  # prints generic MxN-matrix.

    expandedCoeffMatrix = getInput(expandedCoeffMatrix)  # Populates matrix with user inputs.

    printGivenMatrix(expandedCoeffMatrix)  # Prints the given matrix as Ax=b.

    solution = solve3x3System(expandedCoeffMatrix)  # solves system using Cramer's rule.

    # prints solution:
    for i, x in enumerate(solution):
        print(f"{chr(ord('x') + i)} = {x:4}")

if __name__ == "__main__":
    main()  # calls main function.


# example run:
"""
Dette programmet tar inn et likningsystem med 3 likninger
og 3 ukjente i form av en utvidet koeffisientmatrise:
|a b c d|
|e f g h|
|i j k l|
Skriv inn element 'a' og trykk 'enter': 1
Skriv inn element 'b' og trykk 'enter': -2
Skriv inn element 'c' og trykk 'enter': 1
Skriv inn element 'd' og trykk 'enter': 1
Skriv inn element 'e' og trykk 'enter': 3
Skriv inn element 'f' og trykk 'enter': -5
Skriv inn element 'g' og trykk 'enter': 3
Skriv inn element 'h' og trykk 'enter': 0
Skriv inn element 'i' og trykk 'enter': -1
Skriv inn element 'j' og trykk 'enter': 1
Skriv inn element 'k' og trykk 'enter': 0
Skriv inn element 'l' og trykk 'enter': 4
| 1.0 -2.0  1.0 | |x|   | 1.0|
| 3.0 -5.0  3.0 | |y| = | 0.0|
|-1.0  1.0  0.0 | |z|   | 4.0|
x =  1.0
y = -7.0
z = -3.0
"""
