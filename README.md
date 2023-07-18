# Matrix Row Operations

I made this simple command line program to help me do my homework faster for my Matrix and Linear Algebra course by performing the arithmetic for elementary row operations. I still have to determine the next steps, the operations are simply done on each entry of the row for me...perfectly

## Use

The program will prompt the user to enter information during the `READ` stage. Entry entries of the matrix and separate by a space. After pressing `enter`, it will prompt again. Enter the same amount of numbers and continue until all rows have been entered. Press `enter` without any entry to display the matrix and enter `op` (operation) mode

Consider the following example matrix output after the `READ` stage has been completed

```py
[[ 2.  8. -5.  3.]
 [10.  4.  9.  9.]
 [ 3. -1.  0.  2.]]
```

- To perform a type 1 elementary row operation (swap two rows of the matrix), enter the numbers. Examples: `12` `31`
- To perform a type 2 elementary row operation (multiply/divide a row by a scalar), enter the row number followed by `x` or `/` and the scalar. Examples: `2x3` `3x-0.5` `1/2`
- To perform a type 3 elementary row operation (add a row to another row), enter the row to be added, then `]`, then the target row. Examples: `1]2` `3]5`
- To combine type 2 and type 3 operations, enter the type 2 operation, then `]`, then the target of the type 3 operation. Examples: `1x4]2` `2/-2]3` `5/-1.5]1`
- To negate a row, type `-` then the row number: Examples: `-2`

  ## How I used it

  Mostly to bring matrices to Reduced Row Echelon Form. We practiced plenty!
