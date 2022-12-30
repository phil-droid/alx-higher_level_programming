#!/usr/bin/python3

def matrix_mul(m_a, m_b):
    """
    Define two matrix m_a and m_b in program
    Define an empty matrix to store multiplication result
    Using nested for loop method on m_a & m_b matrix
    Storing multiplication result in empty matrix
    Printing multiplication result in the output
    """

    if m_a != list:
        raise TypeError("m_a must be a list")
    if m_b != list:
        raise TypeError("m_b must be a list")
    if m_a == [] or m_a ==[[]]:
        raise ValueError(" m_a can't be empty")

    if m_b == [] or m_b == [[]]:
        raise ValueError(" m_b can't be empty")

    if type(m_a) == float or type(m_b) == float:
        m_a = int(m_a)
        m_b = int(m_b)


    if type(m_a) != int:
        raise TypeError("a must be an integer")
    
    elif type(m_b) != int:
        raise TypeError("b must be an integer")
        
    if len(m_a) != len(m_b):
        raise TypeError("each row of m_a must be of the same size or each row of m_b must be of the same size")
        
    column_m_a =  len(m_a[0])
    column_m_b =  len(m_b[0])
        
    if column_m_b != len(m_a[0]):
        raise ValueError("m_a and m_b can't be multiplied")

    m_a = [[2, 1, 5],
          [2, 1, 7],
          [3, 4, 6]]

    m_b = [[5, 6, 3],
          [1, 4, 2],
          [2, 8, 5]]

    mul_Result = [[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for n in range(len(m_b)):
                mul_Result[i][j] += m_a[i][n] * m_b[n][j]

    print("The multiplication result of matrix m_a and m_b is: ")
    for result in mul_Result:
        print(result)
