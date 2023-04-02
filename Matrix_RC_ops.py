'''
Simple program to help me out with matrix row operations for linear algebra
Useful for getting to REF / RREF while showing work
No more arithmetic mistakes!
Also first time using numpy for a respectable project

Maverick Reynolds
01-12-2023

'''

import re
import numpy as np

'''
Regex for all groups:
^([1-9])(?:([x\/])(\-?0*[1-9]+0*))?(?:([\s\]])?([1-9]))?$
'''

# Read raw matrix values
def main():
    while True:
        Matrix = get_matrix_from_user()
        nrows, _ = np.shape(Matrix)

        print('\nMATRIX:')
        print(Matrix)
        print()

        # Get line and determine operation type
        while (ln := input('OP > ')) != 'new':
            if match := re.fullmatch('^([1-9])\s?(\d)$', ln):
                # Matches '4 6', swap rows, Type 1
                row1, row2 = int(match.group(1))-1, int(match.group(2))-1
                if row1 < nrows and row2 < nrows:
                    Matrix[[row1, row2]] = Matrix[[row2, row1]]

            elif match := re.fullmatch('^([1-9])([x\/])(-?0*[1-9]+0*)$', ln):
                # Matches 3x-0.5, mult row by non-zero scalar, type 2
                row, op, fact = int(match.group(1))-1, match.group(2), float(match.group(3))
                if row < nrows:
                    if op == 'x':
                        Matrix[row] *= fact
                    elif op == '/':
                        Matrix[row] /= fact

            elif match := re.fullmatch('^([1-9])\]([1-9])$', ln):
                # Matches 4]5, add row to another, type 3
                row1, row2 = int(match.group(1))-1, int(match.group(2))-1
                if row1 < nrows and row2 < nrows:
                    Matrix[row2] = np.add(Matrix[row2], Matrix[row1])
            
            elif match := re.fullmatch('^([1-9])([x\/])(-?0*[1-9]0*)\]([1-9])$', ln):
                # Matches 1x-2]3, combine type 2 and type 3 operations
                row1, op, fact, row2 = int(match.group(1))-1, match.group(2), float(match.group(3)), int(match.group(4))-1
                if row1 < nrows and row2 < nrows:
                    if op == 'x':
                        op_row = Matrix[row1] * fact
                    elif op == '/':
                        op_row = Matrix[row1] / fact

                    Matrix[row2] = np.add(Matrix[row2], op_row)

            elif match := re.fullmatch('^-(\d)$', ln):
                # Matches -4, make a row negative
                row = int(match.group(1))-1
                if row < nrows:
                    Matrix[row] *= -1.0
                    
            print(Matrix)
            print()


def get_matrix_from_user():
    matrix = None
    
    while ln := input('READ > '):
        row = [int(x) for x in ln.split()]

        if matrix is None:
            matrix = np.array(row).astype('float64')
            num_cols = len(row)
        elif len(row) == num_cols:
            matrix = np.vstack((matrix, row))
            
        print(matrix)
        print()
    
    return matrix



if __name__ == '__main__':
    main()

